# flask_api_example

<h3>How to run the project after clone it?</h3>
<ul>
  <li>to build de image: docker build -t flask-smorest-api .</li>
  <li>to run the container: docker run -dp 5000:5000 -w /app -v "$(pwd):/app" flask-smorest-api</li>
</ul>
<p>Now you are able to make requests on 5000 port</p>
