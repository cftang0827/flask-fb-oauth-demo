# flask-fb-oauth-demo
A quick demo for facebook oauth third party login with flask. 


### Create localhost https certificate for testing

- Install `mkcert` on MacOS for creating local version certificate
```sh
brew install mkcert
```
- Then create a localhost cert 

```sh
mkcert localhost 
```

- Then you will get the cert file
```sh
localhost.pem
localhost-key.pem
```

### Install requirements
```sh
pip install -r requirements.txt
```

### Lauch Flask test app
```sh
python app.py
```
and click `fb login` link, and you will get `access_token` for facebook login. 