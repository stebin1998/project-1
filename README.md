# BTP405 - Project Submission
**Student Name: Stebin George**

## Technologies Employed
- **Primary Programming Language:** Python
- **Database Management System:** MySQL
- **Source Code Management:** Git
- **Software Containerization:** Docker
- **REST API Verification Tools:** curl / Invoke-RestMethod for PowerShell users

## Setting Up MySQL Using Docker
```bash
docker pull container-registry.oracle.com/mysql/community-server:latest
```
```bash
docker run --name=mysql_server -p 3306:3306 -e MYSQL_ROOT_PASSWORD=my_password --restart unless-stopped -d container-registry.oracle.com/mysql/community-server:latest
```

### Handling GET Requests:
```python
def handle_GET(self):
    self.set_http_response()
    cursor.execute("SELECT health_id, status, description FROM HEALTH")
    for (health_id, status, description) in cursor:
        self.wfile.write(f"{health_id}, {status}, {description}".encode('utf-8'))
```
#### Testing API (PowerShell):
```powershell
Invoke-RestMethod -Uri http://localhost:8010 
```
#### Using curl for Testing:
```bash
curl http://127.0.0.1:8010 
```

### Processing PUT Requests:
```python
def handle_PUT(self):
    self.set_http_response()
    cursor.execute("INSERT INTO HEALTH (STATUS, DESCRIPTION) VALUES ('Excellent', 'Great job, keep it up.')")
    cnx.commit()
```
#### PUT Test (PowerShell):
```powershell
Invoke-RestMethod -Uri http://localhost:8010 -Method PUT 
```
#### Using curl for PUT Testing:
```bash
curl -X PUT http://127.0.0.1:8010 
```

### Managing POST Requests:
```python
def handle_POST(self):
    self.set_http_response()
    cursor.execute("UPDATE HEALTH SET DESCRIPTION = 'Aim for a balanced diet' WHERE STATUS = 'Excellent'")
    cnx.commit()
```
#### POST Testing (PowerShell):
```powershell
Invoke-RestMethod -Uri http://localhost:8010 -Method POST 
```
#### curl Command for POST Testing:
```bash
curl -X POST http://127.0.0.1:8010 
```

### Docker Image Creation:
```bash
docker build -t health_app/v1 .
``` 
### Starting a Docker Container:
```bash
docker run -p 8010:8010 health_app/v1
```

