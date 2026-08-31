# Deployment

- Een **Azure VM** met Debian.
- Java 21 al geïnstalleerd.
- Gebruiker **quintor** met SSH-toegang.
- Poort **8080** opengezet in Azure → Netwerken → Inkomende poortregel.'
- WW: QuintorCodaro1!

---

```bash
cd backend
mvn -DskipTests clean package
```

```bash
scp target/declaraties-backend.war quintor@172.160.249.155:/tmp/ROOT.war
ssh -t quintor@172.160.249.155 '
  sudo systemctl stop tomcat10 || true;
  sudo rm -rf /var/lib/tomcat10/webapps/ROOT*;
  sudo mv /tmp/ROOT.war /var/lib/tomcat10/webapps/ROOT.war;
  sudo chown tomcat:tomcat /var/lib/tomcat10/webapps/ROOT.war;
  sudo systemctl start tomcat10;
'
```

```bash
curl -i http://localhost:8080/api/claims
```

---

```bash
npm run build
```

```bash
scp -r dist quintor@172.160.249.155:/tmp/frontend
ssh -t quintor@172.160.249.155 '
  sudo rm -rf /var/lib/tomcat10/webapps/ROOT/*;
  sudo cp -r /tmp/frontend/* /var/lib/tomcat10/webapps/ROOT/;
  sudo chown -R tomcat:tomcat /var/lib/tomcat10/webapps/ROOT;
'
```


```
http://172.160.249.155:8080/
```

```
http://172.160.249.155:8080/api/claims
```
