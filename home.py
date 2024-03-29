 <!DOCTYPE html>
    <html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
        Docker Web App
    </title>
    
    <style>
        body, html {
        height: 100%;
        margin: 0;
        font-family: Arial, Helvetica, sans-serif;
    }

    * {
        box-sizing: border-box;
    }

    .bg-image {
        /* The image used */
        background-image: url("docker-to-kube.png");
        
        /* Add the blur effect */
        filter: blur(8px);
        -webkit-filter: blur(8px);
        
        /* Full height */
        height: 100%; 
        
        /* Center and scale the image nicely */
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }

    /* Position text in the middle of the page/image */
    .bg-text {
        background-color: rgb(0,0,0); /* Fallback color */
        background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
        color: white;
        font-weight: bold;
        border: 3px solid #f1f1f1;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 2;
        width: 80%;
        padding: 20px;
        text-align: center;
    }

    
    .h2
    {
    position:absolute;
    top: -150px;
    right: 3px;
    padding-bottom: 100px;
    font-size: 8em;
    color: rgba(225, 225, 225, 0.55);
    pointer-events: none;
    }

    .h3{
        color: white;
        font-size: 1.8em;
        margin-top: 100px;
    }
    .btn {
        width: 200px;
        height: 100px;
        border: 5px solid #157ba3;
        border-radius: 100px;
        font-size: x-large;
    }

    #b1 {
        float: left;
        margin-left: 250px;
        margin-top: 15px;
    }
    #b2 {
        float: right;
        margin-right: 250px;
    }

    .btn:hover{
        background-color: rgb(25, 124, 218); 
        border: 7px solid #f1f1f1;
    }

    .btn:active{
        background-color: aquamarine;
        box-shadow: 0 5px #6666;
        transform: translateY(5px);
    }
    </style>
    </head>
    <body>

    <div class="bg-image"></div>

    <div class="bg-text">
        <center><h1 style="color: black;" >Welcome to the World of DevOps!</h1></center>
        <h2>Select the technology you want to use..</h2>
            <div>
                <button id="b1" class="btn" onclick="docker();">Docker</button>
                </br>
                <button id="b2" class="btn" onclick="kube();">Kubernetes</button>
          </div>
    </div>

    </div>
    <script>
        function docker()
        {
         window.location="http://192.168.56.106/docker.html"
        }
   
        function kube()
        {
         window.location="http://192.168.56.106/k8s.html"
        }
    </script>
    </body>
    </html>
