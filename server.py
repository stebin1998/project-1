from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector

def get_db_connection():
    """Establishes and returns a MySQL database connection."""
    return mysql.connector.connect(user='root', password='secret', host='127.0.0.1', database='HealthRecords')

def initialize_db():
    """Creates the HEALTH table if it doesn't exist."""
    with get_db_connection() as conn:
        with conn.cursor() as cursor:
            create_stmt = """
            CREATE TABLE IF NOT EXISTS HEALTH (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                STATUS VARCHAR(15) NOT NULL,
                DETAILS VARCHAR(100) NOT NULL
            )"""
            cursor.execute(create_stmt)
            conn.commit()

class HealthRequestHandler(BaseHTTPRequestHandler):
    def set_headers(self, content_type='text/html'):
        """Sets basic HTTP headers for the response."""
        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """Handles GET requests by fetching health records from the database."""
        self.set_headers()
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT ID, STATUS, DETAILS FROM HEALTH")
                    for (id, status, details) in cursor:
                        response = f"{id}, {status}, {details}\n"
                        self.wfile.write(response.encode('utf-8'))
        except mysql.connector.Error as err:
            self.wfile.write(f"Error: {err}".encode('utf-8'))

    def do_PUT(self):
        """Handles PUT requests by adding a new health record."""
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("INSERT INTO HEALTH (STATUS, DETAILS) VALUES ('Okay', 'Routine check-up suggested.')")
                    conn.commit()
            self.set_headers()
            self.wfile.write("Record added successfully.".encode('utf-8'))
        except mysql.connector.Error as err:
            self.wfile.write(f"Error: {err}".encode('utf-8'))

    def do_POST(self):
        """Handles POST requests by updating an existing health record."""
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute("UPDATE HEALTH SET DETAILS = 'Follow a healthier lifestyle.' WHERE STATUS = 'Okay'")
                    conn.commit()
            self.set_headers()
            self.wfile.write("Record updated successfully.".encode('utf-8'))
        except mysql.connector.Error as err:
            self.wfile.write(f"Error: {err}".encode('utf-8'))


def run(server_class=HTTPServer, handler_class=HealthRequestHandler, port=8010):
    """Runs the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server started on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Server is stopping...')
        httpd.server_close()
        print('Server stopped.')

if __name__ == '__main__':
    initialize_db()
    run()

