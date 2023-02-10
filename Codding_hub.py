from bottle import Bottle
from bottle import run, template
app= Bottle()

@app.route("/")
def home():
    return template("""
<style type="text/css">
 @font-face {
  font-family: 'Material Icons';
  font-style: normal;
  font-weight: 400;
  src: url(https://fonts.gstatic.com/s/materialicons/v128/flUhRq6tzZclQEJ-Vdg-IuiaDsNcIhQ8tQ.woff2) format('woff2');
}
#name{font-weight: bold; font-size: 20px; margin-left: 400px}
span> .dv1> char{
    padding-left: 5px;
    padding-right: 5px;
    border-radius: 1px;
    border-image-outset: 1px;}
    
span> .div2> char{
    padding-left: 5px;
    padding-right: 5px;
    border-radius: 1px;
    border-image-outset: 1px;}

.material-icons {
  font-family: 'Material Icons';
  font-weight: normal;
  font-style: normal;
  font-size: 24px;
  line-height: 1;
  letter-spacing: normal;
  text-transform: none;
  display: inline-block;
  white-space: nowrap;
  word-wrap: normal;
  direction: ltr;
  -webkit-font-feature-settings: 'liga';
  -webkit-font-smoothing: antialiased;
  background: transparent;
}
</style>
<body>
<nav>
    <a href='#' style='text-decoration:none'> </a>
    <div class='list'>
      <button class='btn' id="btn">≡</button>
    <ul style='list-style-type:none' class="navs">
        <li id="li1"><a herf='#'><i class='material-icons'>home</i>Home</a></li>
        <li id="li2"><a href='#'></a><i class='material-icons'>info</i>About</li>
        <li id="li3"><a href='#'></a><i class='material-icons'>web_assert</i>Articles</li>
    </ul>
    </div>
    <span id="name">&nbsp<div class="dv1" style="margin-left: 420px;">
    <char id="c">C</char><char id="o">o</char><char id="d">d</char><char id="dd">d</char><char id="i">i</char><char id="n">n</char><char id="g">g</char></div>
    &nbsp <br><div class ="div2" style="margin-left: 470px;">
    <char id="h">H</char><char id="u">u</char><char id="b">b</char></div></span>
    <div style="border-radius: 20px; background-color:yellow; text-align: right; margin-left: 940px" height=150 width=50 id="theme">fif</div>
    <br>
  </nav>
<br><br>
<div class='input-cnt'>
      <i class='material-icons' id="search" style="background: transparent;">search</i>
      <input type='text' placeholder='Search here...' id="Search-bar"/>
</div>
<div id="py">
<div id='python' class='python'>
    <char id='name' class='name' style="float: left">Python</char>
    <button id='b1' class="btns">
        <i class='material-icons'>expand_more</i></button>
    <p class='python-code'>
<pre style="background: transparent">
>>> <b style="color:orange; background: transparent">import</b> os, setuptools
>>> <b style="color:orange; background: transparent">print</b>(<code style="color: yellow">"Hello world"</code>)
<code style="color: yellow; background: transparent;">"Hello world"</code>
>>> os.<b style="color:orange; background: transparent">system</b>(<a style="color: yellow">"sh"</a>) <c style="color:grey; background:transparent"># or</c>
$ exit

>>> setuptools.<b style="color:orange; background: transparent">setup</b>()
$ exit
</pre></p>
</div></div><br>

<div class="3d_link" id="3d_link">
    3D Shapes area and volume calculation
    <ul list-style-type="circle">
        <li>Sphere</li>
        <li>Cube</li>
        <li>Cuboid</li>
        <li>Cylinder</li>
    </ul>
    <a href="3d.html" id="link">3D Shapes page</a>
</div>
  <footer class="cookies" id="cook" style="position:fixed; bottom:0px;"><div class="divs"><div>Cookies</div><div>This is Footer.This is demo.
    Click Ok to accept our cookies and Cancel to
    to decline cookies.</div></div>
    <button id="Ok"class="cook_btn">Ok</button>
    <button id="Cancel" class="cook_btn">Cancel</button>
  </footer>
  <script>
  var cook=document.getElementById("cook");
cook.style.display ="block"
document.getElementById("Ok").onclick= function() {
alert("Thanks for accepting Cookies");
cook.style.display="none";
    };

document.getElementById("Cancel").onclick = function() {
    alert("Please accept cookies on your next visit");
cook.style.display="none";
    };
document.getElementById('b1').onclick= function () {
    var elem=document.getElementById("py");
    
    if (elem.style.height== "230px") {
        elem.style= "height: 47px; overflow: hidden; transition-duration: 1s";
    }

    else {
        elem.style= "height: 230px; overflow: hidden; transition-duration: 1s";
    }
};;
</script>
  <script>
 window.boxSizing = "border-box";
document.body.style = "display: flex; min-height: 100vh; flex-direction: column;";

document.body.style.backgroundColor = "black";
            //color: white
document.body.style.color = "white";
            // transparent border border image
            // Codding hub main Label
document.getElementById("c").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("o").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("d").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("dd").style="border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("i").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("n").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("g").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("h").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("u").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
document.getElementById("b").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
            // navigation bar
document.getElementsByClassName("list")[0].style = "float: left; position:relative; display:inline-block;";
document.getElementById("btn").style = "color:white; background:#050505; border:5px solid #090909;width:90px; font-size:30px; height:70px; border-radius: 10px;";
document.getElementsByClassName("navs")[0].style = "color:grey; background:black; padding-left:0; text-align:right; position:absolute; width:0; height:100px; transition:width 0.5s; overflow:auto;";
            // expending navigation drawer
document.getElementById("btn").onmouseenter = function () {
    document.getElementsByClassName("navs")[0].style = "padding-left:0; height:100px; width:90px; text-align:justify; color:grey; background:black; position:absolute; height:100px; transition:width 0.5s; overflow:auto;";
    document.getElementById("btn").style = "color:white;background:#090909; border:5px solid RoyalBlue; font-size:30px; height:70px; border-radius: 10px; width:90px;";
};
            // selecting option from navigation drawer
document.getElementById("li1").onmouseenter = function () {
    document.getElementById("li1").style = "color:white;";
};
document.getElementById("li2").onmouseenter = function () {
    document.getElementById("li2").style = "color:white;";
};
document.getElementById("li3").onmouseenter = function () {
    document.getElementById("li3").style = "color:white;";
};
            // closing navigation drawer
document.getElementById("btn").ondblclick = function () {
    document.getElementById("btn").style = "color:white;background:#090909;border:5px solid #090909;width:90px; padding:0px; font-size:30px; height:70px; border-radius: 10px";
    document.getElementsByClassName("navs")[0].style = "color:grey; background:black; padding-left:0; text-align:right; position:absolute; width:0; height:100px; transition:width 0.5s; overflow:auto;";
};
            // unselecting an option from navigation drawer
document.getElementById("li1").onmouseleave = function () {
    document.getElementById("li1").style = "color:grey;";
};
document.getElementById("li2").onmouseleave = function () {
    document.getElementById("li2").style = "color:grey;";
};
document.getElementById("li3").onmouseleave = function () {
    document.getElementById("li3").style = "color:grey;";
};
            // Cookie Div
document.getElementsByClassName("divs")[0].style = "color:#fff; margin-bottom:0px; width:100%; height: 110px; padding:0px; text-align:center; margin-top:450px";
document.getElementsByClassName("divs")[0].firstChild.style = "font-size: 150%";
            // Cookie buttons
document.getElementsByClassName("cook_btn")[0].style = "color: #fff; border-radius:20px; background:#111; margin-bottom:0px; font-size:120%;";
document.getElementsByClassName("cook_btn")[1].style = "color: #fff; border-radius:20px; background:#111; margin-bottom:0px; font-size:120%;";

            // Search bar
document.getElementsByClassName("input-cnt")[0].style.display = "flex";
document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: grey; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid lightgrey; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 60%; color: white; transition: width .5s;";
            // Searching
document.getElementById("Search-bar").onmouseenter = function() {
    document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: #0076ff; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
    document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid #0076ff; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 100%; color: white; transition: width .5s;";
};
            // Deselecting Search bar
document.getElementById("Search-bar").onmouseleave = function() {
    document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: grey; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
    document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid lightgrey; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 60%; color: white; transition: .5s;";
};
            // Python Code Label
document.getElementById("py").style = "margin-top: 10px; border: 3px solid #999; background: #222; height: 230px; border-radius: 20px; color: white;";
document.getElementsByClassName("python-code")[0].style = "background:transparent; padding: 5px";
document.getElementById("b1").style = "width:25px; border: none; background: transparent; overflow: hidden; display:flex; flex: column; font-weight:bold;";
document.getElementsByClassName("python")[0].style = "margin-top: 10px;";
document.getElementsByClassName("btns")[0].style= "color: white; background: transparent; border: 2px solid transparent;";
            // 3d.html function & link
document.getElementById("3d_link").style= "color: white";
document.getElementById("link").style= "color: white; text-decoration: none;";

function theming() {
    // Dark Theme
    document.getElementById("theme").ondblclick = function () {
        document.body.style.backgroundColor = "black";
        //color: white
        document.getElementById("name").style.color = "white";
        // transparent border border image
        // Codding hub main Label
        document.getElementById("c").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("o").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("d").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("dd").style= "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("i").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("n").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("g").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("h").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("u").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        document.getElementById("b").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, blue, red) 1 stretch;";
        // navigation bar
        document.getElementsByClassName("list")[0].style = "float: left; position:relative; display:inline-block;";
        document.getElementById("btn").style = "color:white; background:#050505; border:5px solid #090909;width:90px; font-size:30px; height:70px; border-radius: 10px;";
        document.getElementsByClassName("navs")[0].style = "color:grey; background:black; padding-left:0; text-align:right; position:absolute; width:0; height:100px; transition:width 0.5s; overflow:auto;";
        // expending navigation drawer
        document.getElementById("btn").onmouseenter = function () {
            document.getElementsByClassName("navs")[0].style = "padding-left:0; height:100px; width:90px; text-align:justify; color:grey; background:black; position:absolute; height:100px; transition:width 0.5s; overflow:auto;";
            document.getElementById("btn").style = "color:white;background:#090909; border:5px solid RoyalBlue; font-size:30px; height:70px; border-radius: 10px; width:90px;";
        };
        // selecting option from navigation drawer
        document.getElementById("li1").onmouseenter = function () {
            document.getElementById("li1").style = "color:white;";
        };
        document.getElementById("li2").onmouseenter = function () {
            document.getElementById("li2").style = "color:white;";
        };
        document.getElementById("li3").onmouseenter = function () {
            document.getElementById("li3").style = "color:white;";
        };
        // closing navigation drawer
        document.getElementById("btn").ondblclick = function () {
            document.getElementById("btn").style = "color:white;background:#090909;border:5px solid #090909;width:90px; padding:0px; font-size:30px; height:70px; border-radius: 10px";
            document.getElementsByClassName("navs")[0].style = "color:grey; background:black; padding-left:0; text-align:right; position:absolute; width:0; height:100px; transition:width 0.5s; overflow:auto;";
        };
        // unselecting an option from navigation drawer
        document.getElementById("li1").onmouseleave = function () {
            document.getElementById("li1").style = "color:grey;";
        };
        document.getElementById("li2").onmouseleave = function () {
            document.getElementById("li2").style = "color:grey;";
        };
        document.getElementById("li3").onmouseleave = function () {
            document.getElementById("li3").style = "color:grey;";
        };
        // Cookie Div
        document.getElementsByClassName("divs")[0].style = "color:#fff; margin-bottom:0px; width:100%; height: 110px; padding:0px; text-align:center; margin-top:450px";
        document.getElementsByClassName("divs")[0].firstChild.style = "font-size: 150%";
        // Cookie buttons
        document.getElementsByClassName("cook_btn")[0].style = "color: #fff; border-radius:20px; background:#111; margin-bottom:0px; font-size:120%;";
        document.getElementsByClassName("cook_btn")[1].style = "color: #fff; border-radius:20px; background:#111; margin-bottom:0px; font-size:120%;";
        // Search bar
        document.getElementsByClassName("input-cnt")[0].style.display = "flex";
        document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: grey; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
        document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid lightgrey; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 60%; color: white; transition: width .5s;";
        // Searching
        document.getElementById("Search-bar").onmouseenter = function() {
            document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: #0076ff; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
            document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid #0076ff; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 100%; color: white; transition: width .5s;";
        };
        // Deselecting Search bar
        document.getElementById("Search-bar").onmouseleave = function() {
            document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: grey; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
            document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid lightgrey; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 60%; color: white; transition: .5s;";
        };
        // Python Code Label
        document.getElementById("py").style = "margin-top: 10px; border: 3px solid #333; background: #181818; height: 230px; border-radius: 20px; color: white;";
        document.getElementsByClassName("python-code")[0].style = "background: transparent; padding: 5px";
        document.getElementById("b1").style = "width:25px; border: none; background: transparent; overflow: hidden; display:flex; flex: column; font-weight:bold;";
        document.getElementsByClassName("python")[0].style = "margin-top: 10px;";
        document.getElementsByClassName("btns")[0].style= "color: white; background: transparent; border: 2px solid transparent;";
        // 3d.html function & link
        document.getElementById("3d_link").style= "color: white";
        document.getElementById("link").style= "color: white; text-decoration: none;";
    };

     // Light theme
    document.getElementById("theme").onclick = function () {
        document.body.style.backgroundColor = "white";
        //color: black
        document.getElementById("name").style.color = "black";
        // transparent border border image
        // Codding hub main Label
        document.getElementById("c").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("o").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("d").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("dd").style= "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("i").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("n").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("g").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("h").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("u").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        document.getElementById("b").style = "border: 4px solid transparent; border-image: linear-gradient(to top left, orange, #f2b) 1 stretch;";
        // navigation bar
        document.getElementsByClassName("list")[0].style = "float: left; position:relative; display:inline-block;";
        document.getElementById("btn").style = "color:black; background:#f5f5f5; border:5px solid #ccc; width:90px; font-size:30px; height:70px; border-radius: 10px;";
        document.getElementsByClassName("navs")[0].style = "color:grey; background:#ccc; padding-left:0; text-align:right; position:absolute; width:0; height:100px; transition:width 0.5s; overflow:auto;";
        // expending navigation drawer
        document.getElementById("btn").onmouseenter = function () {
            document.getElementsByClassName("navs")[0].style = "padding-left:0; height:100px; width:90px; text-align:justify; color:grey; background:#ccc; position:absolute; height:100px; transition:width 0.5s; overflow:auto;";
            document.getElementById("btn").style = "color:black; background:#ccc; border-radius: 10px; border:5px solid orange; font-size:30px; height:70px; border-radius: 10px; width:90px;";
        };
        // selecting option from navigation drawer
        document.getElementById("li1").onmouseenter = function () {
            document.getElementById("li1").style = "color:black;";
        };
        document.getElementById("li2").onmouseenter = function () {
            document.getElementById("li2").style = "color:black;";
        };
        document.getElementById("li3").onmouseenter = function () {
            document.getElementById("li3").style = "color:black;";
        };
        // closing navigation drawer
        document.getElementById("btn").ondblclick = function () {
            document.getElementById("btn").style = "color:black; background:#f5f5f5; border:5px solid #ccc; width:90px; padding:0px; font-size:30px; height:70px; border-radius: 10px";
            document.getElementsByClassName("navs")[0].style = "color:grey; background:#ccc; padding-left:0; text-align:right; position:absolute; width:0; height:100px; transition:width 0.5s; overflow:auto;";
        };
        // unselecting an option from navigation drawer
        document.getElementById("li1").onmouseleave = function () {
            document.getElementById("li1").style = "color:grey;";
        };
        document.getElementById("li2").onmouseleave = function () {
            document.getElementById("li2").style = "color:grey;";
        };
        document.getElementById("li3").onmouseleave = function () {
            document.getElementById("li3").style = "color:grey;";
        };
        // Cookie Div
        document.getElementsByClassName("divs")[0].style = "color:#000; margin-bottom:0px; width:100%; height: 110px; padding:0px; text-align:center; margin-top:450px";
        document.getElementsByClassName("divs")[0].firstChild.style = "font-size: 150%";
        // Cookie buttons
        document.getElementsByClassName("cook_btn")[0].style = "color: #000; border-radius:20px; background:#eee; margin-bottom:0px; font-size:120%;";
        document.getElementsByClassName("cook_btn")[1].style = "color: #000; border-radius:20px; background:#eee; margin-bottom:0px; font-size:120%;";
        // Search bar
        document.getElementsByClassName("input-cnt")[0].style.display = "flex";
        document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: grey; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
        document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid lightgrey; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 60%; color: black; transition: width .5s;";
        // Searching
        document.getElementById("Search-bar").onmouseenter = function() {
            document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: #0076ff; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
            document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid #0076ff; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 100%; color: black; transition: width .5s;";
        };
        // Deselecting Search bar
        document.getElementById("Search-bar").onmouseleave = function() {
            document.getElementById("search").style = "min-width: 40px; padding: 10px; text-align: center; background: grey; border-top-left-radius: 20px; border-bottom-left-radius: 20px;";
            document.getElementById("Search-bar").style = "background: transparent; outline: none; border: none; padding: 10px; border: 1px solid lightgrey; border-top-right-radius: 20px; border-bottom-right-radius: 20px; width: 60%; color: black; transition: .5s;";
        };
        // Python Code Label
        document.getElementById("py").style= "margin-top: 10px; border: 3px solid #ccc; background: #e8e8e8; height: 230px; border-radius: 20px; color: black;";
        document.getElementsByClassName("python-code")[0].style = "background:transparent; padding: 5px";
        document.getElementById("b1").style = "width:25px; border: none; background: transparent; overflow: hidden; display:flex; flex: column; font-weight:bold;";
        document.getElementsByClassName("python")[0].style = "margin-top: 10px;";
        document.getElementsByClassName("btns")[0].style= "color: black; background: transparent; border: 2px solid transparent";
        // 3d.html function & link
        document.getElementById("3d_link").style= "color: black";
        document.getElementById("link").style= "color: black; text-decoration: none;";
    };
};
theming();
  </script>
  </body>
""")

run(app, host="0.0.0.0", port=8743)