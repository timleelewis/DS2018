<!DOCTYPE html>
<html>
<head>
<title>Simple Viewer provided by TheCubicle.US</title>

<style>

select {
	border: 0px;
    outline: 0px;
    font-size: 30px;
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    }

.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    text-align: center;
}

#byte_content {
    margin: 5px 0;
    max-height: 100px;
    overflow-y: auto;
    overflow-x: hidden;
  }

h3 {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    text-align: center;
}

#customers {
    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
    border-collapse: collapse;
    table-layout: auto;
    width: 96%;
    margin-left:2%; 
    margin-right:2%;
}

#customers td, #customers th {
    border: 3px solid #000000;
    padding: 20px;
    
}



#customers tr:hover {background-color: #ddd;}


</style>
</head>
<body>

</br>

<input type='file' id='fileinput'>
<input type='button' id='btnLoad' value='Load' onclick='loadFile();'>



</br>
</br>
</br>
<h3> 
<select name="Events/Groups" id="chooseEvent" onchange="loadSheet();">
<option>Load competition .json file to start!</option>
</select> 
</h3>
</br>
</br>



<table id="customers">
  
  <tr>
    <td width="5%" align="center">1.</td>
    <td id="Scramble1"></td>
    <td width="30%">image</td>
  </tr>
  
  <tr>
    <td align="center">2.</td>
    <td id="Scramble2"></td>
    <td>image</td>
  </tr>
  
  <tr>
    <td align="center">3.</td>
    <td id="Scramble3"></td>
    <td>image</td>
  </tr>
  
  <tr>
    <td align="center">4.</td>
    <td id="Scramble4"></td>
    <td>image</td>
  </tr>
  
  <tr>
    <td align="center">5.</td>
    <td id="Scramble5"></td>
    <td>image</td>
  </tr>
  
  
  

    
  <tr>
        <td align="left" colspan="3">Extra Scrambles:</td>
  </tr>
    
 
  
  <tr>
    <td align="center">E1.</td>
    <td id="ScrambleE1"></td>
    <td>image</td>
  </tr>
  
  <tr>
    <td align="center">E2.</td>
    <td id="ScrambleE2"></td>
    <td>image</td>
  </tr>

</table>



<div class="footer">
<img src="https://i.imgur.com/YHONVBb.png" alt="Chris Tran made dis" style="width:300px;height:75px;" align="right">
</div>




<script>
  var newArr;
  var sheetCount;
  var currentSheet = 0;
  
  

  function loadFile() {
    var input, file, fr;

    if (typeof window.FileReader !== 'function') {
      alert("The file API isn't supported on this browser yet.");
      return;
    }

    input = document.getElementById('fileinput');
    if (!input) {
      alert("Um, couldn't find the fileinput element.");
    }
    else if (!input.files) {
      alert("This browser doesn't seem to support the `files` property of file inputs.");
    }
    else if (!input.files[0]) {
      alert("Please select a file before clicking 'Load'");
    }
    else {
      file = input.files[0];
      fr = new FileReader();
      fr.onload = receivedText;
      fr.readAsText(file);
    }
    

    function receivedText(e) {
      let lines = e.target.result;
      newArr = JSON.parse(lines);
      
      var sheet = newArr.sheets[0];
      sheetCount = newArr.sheets.length;
      
      
      document.getElementById("Scramble1").innerHTML = sheet.scrambles[0];
      document.getElementById("Scramble2").innerHTML = sheet.scrambles[1];
      document.getElementById("Scramble3").innerHTML = sheet.scrambles[2];
      document.getElementById("Scramble4").innerHTML = sheet.scrambles[3];
      document.getElementById("Scramble5").innerHTML = sheet.scrambles[4];
      
      document.getElementById("ScrambleE1").innerHTML = sheet.extraScrambles[0];
      document.getElementById("ScrambleE2").innerHTML = sheet.extraScrambles[1];
      
      var dropdown = document.getElementById("chooseEvent");
      dropdown.options[0] = null;
      
      for ( var i =0; i < sheetCount; ++i){
      	var iSheet = newArr.sheets[i];
        var groupName = iSheet.title;
      	dropdown[dropdown.length] = new Option(groupName, i);
        	}
    	}
    
    }
    
    
    
    
    
        
    
    function loadSheet(){
        var sheetToLoad = document.getElementById("chooseEvent").value;
        currentSheet = sheetToLoad;
        var sheet = newArr.sheets[currentSheet];
        
        
      	document.getElementById("Scramble1").innerHTML = sheet.scrambles[0];
        document.getElementById("Scramble2").innerHTML = sheet.scrambles[1];
        document.getElementById("Scramble3").innerHTML = sheet.scrambles[2];
        document.getElementById("Scramble4").innerHTML = sheet.scrambles[3];
        document.getElementById("Scramble5").innerHTML = sheet.scrambles[4];
      
        document.getElementById("ScrambleE1").innerHTML = sheet.extraScrambles[0];
        document.getElementById("ScrambleE2").innerHTML = sheet.extraScrambles[1];
    
    }
      
    
    
  
  
  
  
  
  
  
  
  
  
  
  
</script>
</body>
</html>
