function createMatrix(num){

    var arr = [];
  
    // Creates all lines:
    for(var i=0; i < num; i++){
  
        // Creates an empty line
        arr.push([]);
  
        // Adds cols to the empty line:
        arr[i].push( new Array(num));
        
        for(var j=0; j < num; j++){
          // Initializes:
          if(i%2==0 && j%2==0){
            arr[i][j] = '.';
          }
          else{
            arr[i][j] = ' ';  
          }

    }
    }
  
  return arr;
  }
var logoName = [];
var logoPath = [];
var matrix = createMatrix(21);
var path90 ="" ;
var path180="" ;
var path270="" ;
function display(l) {
    var ini = l.split(" ")  ;
    if(ini[0] == "LOGO"){

            //Not in the array
            logoName.push(ini[1]);
            logoPath.push(ini[2]);
            console.log(ini[1]+" defined");
            
        
      
    }
    else if (ini[0] == "ENGRAVE"){
      engrave(ini[1],parseInt(ini[2]),parseInt(ini[3]));
    }
    else if(ini[0] == "SAME") {
      same(ini[1],ini[2]);
    }
    
  }
function engrave(logName, targetX, targetY){

  var logoP ;
  var cursorX = parseInt(targetX);
  var cursorY = parseInt(targetY);
  if (logoName.indexOf(logName) > -1) {
    //In the array!
      
      logoP = logoPath[logoName.indexOf(logName)];
      if(logoP[0] == 'U'){        // BU İLK İŞLEM
        matrix[(cursorX*2)-3][(cursorY*2)-2] = '|';
        cursorX = (cursorX*2)-3;
        cursorY = (cursorY*2)-2;
      }
      else if(logoP[0] == 'R'){
        matrix[(cursorX*2)-2][(cursorY*2)-1] = '-';
        cursorX = (cursorX*2)-2;
        cursorY = (cursorY*2)-1;
      }
      else if(logoP[0] == 'L'){
        matrix[(cursorX*2)-2][(cursorY*2)-1] = '-';
        cursorX = (cursorX*2)-2;
        cursorY = (cursorY*2)-1;
      }
      else{
        matrix[(cursorX*2)-1][(cursorY*2)-2] = '|';
        cursorX = (cursorX*2)-1;
        cursorY = (cursorY*2)-2;
      }
      for(i = 1;i<logoP.length;i++){ // BU İKİNCİ İŞLEM
        if(logoP[i] == 'U'){
          if(logoP[i-1]==('U')){
            matrix[(cursorX)-2][cursorY] = '|';
            cursorX = cursorX-2;
          }
          else if(logoP[i-1]==('D')){
            matrix[(cursorX)][cursorY] = '|';
            cursorX = cursorX;
            cursorY = cursorY;
          }
          else{//r l ise
            if(logoP[i-1]==("L")){
            matrix[(cursorX)-1][cursorY-1] = '|';
            cursorX = cursorX-1;
            cursorY = cursorY-1;
            }
            else{
              matrix[cursorX-1][cursorY+1] = '|';
              cursorX = cursorX-1;
              cursorY = cursorY+1;
            }
        }
      }
        else if(logoP[i] == 'R'){
          if(logoP[i-1]==("U")){
            matrix[cursorX-1][cursorY+1] = '-';
            cursorX = cursorX-1;
            cursorY = cursorY+1;
          }
          else if(logoP[i-1]==("D")){
            matrix[cursorX+1][cursorY+1] = '-';
            cursorX = cursorX+1;
            cursorY = cursorY+1;
          }
          
          else if(logoP[i-1]==("R")){
              matrix[(cursorX)][(cursorY)+2] = '-';
              cursorX = cursorX;
              cursorY = cursorY+2;
            }
          else if(logoP[i-1]==("L")){
              matrix[cursorX][cursorY] = '-';
              cursorX = cursorX;
              cursorY = cursorY;
            }
          }
        else if(logoP[i] == 'L'){
          if(logoP[i-1]==("U")){
            matrix[cursorX-1][cursorY-1] = '-';
            cursorX = cursorX-1;
            cursorY = cursorY-1;
          }
          else if(logoP[i-1]==("D")){
            matrix[cursorX+1][cursorY-1] = '-';
            cursorX = cursorX+1;
            cursorY = cursorY-1;
          }
          else if(logoP[i-1]==("R")){
              matrix[(cursorX)][(cursorY)] = '-';
              cursorX = cursorX;
              cursorY = cursorY;
            }
          else if(logoP[i-1]==("L")){
              matrix[cursorX][cursorY-2] = '-';
              cursorX = cursorX;
              cursorY = cursorY-2;
            }
          }
        
        else{
          if(logoP[i-1]==('U')){
            matrix[(cursorX)][cursorY] = '|';
            cursorX = cursorX;
            cursorY = cursorY;
          }
          else if(logoP[i-1]==('D')){
            matrix[(cursorX)+2][cursorY] = '|';
            cursorX = cursorX+2;
            cursorY = cursorY;
          }
          else{//r l ise
            if(logoP[i-1]==("L")){
            matrix[(cursorX)+1][cursorY-1] = '|';
            cursorX = cursorX+1;
            cursorY = cursorY-1;
            }
            else{
              matrix[cursorX+1][cursorY+1] = '|';
              cursorX = cursorX+1;
              cursorY = cursorY+1;
            }
        }
        }
    }
} 
  for(i = 0 ; i<21;i++){
    for(j = 0 ; j<21; j++){
      process.stdout.write(matrix[i][j]);
    }
    console.log()
  }
 matrix = createMatrix(21);
}
function rotateEngrave(pattern,patternar,cursorX,cursorY){
  patternar = createMatrix(43);
  if(pattern[0] == 'U'){        // BU İLK İŞLEM
    patternar[(cursorX*2)-3][(cursorY*2)-2] = '|';
    cursorX = (cursorX*2)-3;
    cursorY = (cursorY*2)-2;
  }
  else if(pattern[0] == 'R'){
    patternar[(cursorX*2)-2][(cursorY*2)-1] = '-';
    cursorX = (cursorX*2)-2;
    cursorY = (cursorY*2)-1;
  }
  else if(pattern[0] == 'L'){
    patternar[(cursorX*2)-2][(cursorY*2)-1] = '-';
    cursorX = (cursorX*2)-2;
    cursorY = (cursorY*2)-1;
  }
  else{
    patternar[(cursorX*2)-1][(cursorY*2)-2] = '|';
    cursorX = (cursorX*2)-1;
    cursorY = (cursorY*2)-2;
  }
  for(i = 1;i<pattern.length;i++){ // BU İKİNCİ İŞLEM
    if(pattern[i] == 'U'){
      if(pattern[i-1]==('U')){
        patternar[(cursorX)-2][cursorY] = '|';
        cursorX = cursorX-2;
      }
      else if(pattern[i-1]==('D')){
        patternar[(cursorX)][cursorY] = '|';
        cursorX = cursorX;
        cursorY = cursorY;
      }
      else{//r l ise
        if(pattern[i-1]==("L")){
        patternar[(cursorX)-1][cursorY-1] = '|';
        cursorX = cursorX-1;
        cursorY = cursorY-1;
        }
        else{
          patternar[cursorX-1][cursorY+1] = '|';
          cursorX = cursorX-1;
          cursorY = cursorY+1;
        }
    }
  }
    else if(pattern[i] == 'R'){
      if(pattern[i-1]==("U")){
        patternar[cursorX-1][cursorY+1] = '-';
        cursorX = cursorX-1;
        cursorY = cursorY+1;
      }
      else if(pattern[i-1]==("D")){
        patternar[cursorX+1][cursorY+1] = '-';
        cursorX = cursorX+1;
        cursorY = cursorY+1;
      }
      
      else if(pattern[i-1]==("R")){
        patternar[(cursorX)][(cursorY)+2] = '-';
          cursorX = cursorX;
          cursorY = cursorY+2;
        }
      else if(pattern[i-1]==("L")){
        patternar[cursorX][cursorY] = '-';
          cursorX = cursorX;
          cursorY = cursorY;
        }
      }
    else if(pattern[i] == 'L'){
      if(pattern[i-1]==("U")){
        patternar[cursorX-1][cursorY-1] = '-';
        cursorX = cursorX-1;
        cursorY = cursorY-1;
      }
      else if(pattern[i-1]==("D")){
        patternar[cursorX+1][cursorY-1] = '-';
        cursorX = cursorX+1;
        cursorY = cursorY-1;
      }
      else if(pattern[i-1]==("R")){
        patternar[(cursorX)][(cursorY)] = '-';
          cursorX = cursorX;
          cursorY = cursorY;
        }
      else if(pattern[i-1]==("L")){
        patternar[cursorX][cursorY-2] = '-';
          cursorX = cursorX;
          cursorY = cursorY-2;
        }
      }
    
    else{
      if(pattern[i-1]==('U')){
        patternar[(cursorX)][cursorY] = '|';
        cursorX = cursorX;
        cursorY = cursorY;
      }
      else if(pattern[i-1]==('D')){
        patternar[(cursorX)+2][cursorY] = '|';
        cursorX = cursorX+2;
        cursorY = cursorY;
      }
      else{//r l ise
        if(pattern[i-1]==("L")){
          patternar[(cursorX)+1][cursorY-1] = '|';
        cursorX = cursorX+1;
        cursorY = cursorY-1;
        }
        else{
          patternar[cursorX+1][cursorY+1] = '|';
          cursorX = cursorX+1;
          cursorY = cursorY+1;
        }
    }
    }
}
return patternar;
}
function rotate(pattern){
  
  for(var i=0;i<pattern.length;i++){
    if(pattern[i]=='D'){
      path90+='L';
      path180+='U';
      path270+='R';
    }
    else if(pattern[i]=='U'){
      path90+='R';
      path180+='D';
      path270+='L';
    }
    else if(pattern[i]=='R'){
      path90+='D';
      path180+='L';
      path270+='U';
    }
    else{
      path90+='U';
      path180+='R';
      path270+='D';
    }
  }
  
}
function comp(lo1,lo2){
  var bekar = true;
  for(i = 0 ; i<43;i++){
    for(j = 0 ; j<43; j++){
      if(lo1[i][j]!=lo2[i][j]){
        bekar = false;
        break;
      }
    }
  }
  return bekar;
}
function leftto(arr){
  var row = 3;
  for(var i = 0; i<43;i++){
    for(var j = 0;j<43;j++){
      if(arr[j][i]=="|"||arr[j][i]=="-"){
        
        row = i;
      
        return row;
      }
    }
  }
}
function topto(arr){
  var row = 3;
  for(var i = 0; i<43;i++){
    for(var j = 0;j<43;j++){
      if(arr[i][j]=="|"||arr[i][j]=="-"){
        row = i;
        return row;
      }
    }
  }
}
function tran(arr,top,left){
for(var i = 0;i<43;i++){
  for(var j = 0; j<43;j++){
    if((arr[i][j]=="|")||(arr[i][j]=="-")){
      arr[i-top][j-left]=arr[i][j];
      arr[i][j]=" ";
    }
  }
}
return arr;
}
function same(log1,log2){

var path1 = logoPath[logoName.indexOf(log1)];
var path2 = logoPath[logoName.indexOf(log2)];

rotate(path1);
var pat0ar = rotateEngrave(path1,pat0ar,parseInt(11),parseInt(11));
var pat90ar= rotateEngrave(path90,pat90ar,parseInt(11),parseInt(11));
var pat180ar = rotateEngrave(path180,pat180ar,parseInt(11),parseInt(11));
var pat270ar = rotateEngrave(path270,pat270ar,parseInt(11),parseInt(11));
var pat2ar = rotateEngrave(path2,pat2ar,parseInt(11),parseInt(11));


pat0ar = tran(pat0ar,topto(pat0ar),leftto(pat0ar));
pat90ar= tran(pat90ar,topto(pat90ar),leftto(pat90ar));
pat180ar= tran(pat180ar,topto(pat180ar),leftto(pat180ar));
pat270ar= tran(pat270ar,topto(pat270ar),leftto(pat270ar));
pat2ar= tran(pat2ar,topto(pat2ar),leftto(pat2ar));
      
      if(comp(pat0ar,pat2ar)==true){
        console.log("Yes");
        
      }
      else if(comp(pat90ar,pat2ar)==true){
        console.log("Yes");
        
      }
      else if(comp(pat180ar,pat2ar)==true){
        console.log("Yes");
        
      }
      else if(comp(pat270ar,pat2ar)==true){
        console.log("Yes");
        
      }
      else{
        console.log("No")
      }
      
    path90 ="" ;
    path180="" ;
    path270="" ;
    }

var readline = require('readline');
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false
 });
rl.on('line', function (line) {
    display(line);
 });
