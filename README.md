# flask_api_example

<h3>How to run the project after clone it?</h3>
<ul>
  <li>to build de image: docker build -t flask-smorest-api .</li>
  <li>to run the image: docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api sh -c "flask run"<li>
  <li>to run the containers: docker compose up -d</li>
  <li>to run the queue image: docker build -t rest-api-recording-email .</li>
  <li>to run the queue container: docker run -p 3000:3000 rest-api-recording-email sh -c "flask run --host 0.0.
0.0"</li>
</ul>
<p>Now you are able to make requests on 5000 port</p>
