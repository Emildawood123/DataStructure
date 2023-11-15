let Offset_basis = 2166136261;
let Prime = 16777619;
let hash32 = function (data)
{
let arrOfbyte = convert(data);
var hash = Offset_basis;
for (let i = 0; i < arrOfbyte.length; i++)
{
   hash = hash ^ arrOfbyte[i];
   hash = hash * Prime; 
}
return hash;
}

console.log(hash32("emil"));


function convert(string) {
    let output = [];
    for (var i = 0; i < string.length; i++) {
        output.push(string[i].charCodeAt(0).toString(2));
    }
    return output;
  }