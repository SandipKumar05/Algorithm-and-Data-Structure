# Run this file to test all the api calls 
curl http://127.0.0.1:5000/books

cur http://127.0.0.1:5000/book/1

curl -X POST -H "Content-Type: application/json" -d '{"name":"puja","author":"pp"}' http://127.0.0.1:5000/update/1

curl -X PUT -H "Content-Type: application/json" -d '{"name":"puja"}' http://127.0.0.1:5000/update/1

curl -X DELETE http://127.0.0.1:5000/delete/1