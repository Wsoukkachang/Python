const array = [1,2,4];
 
function getMaxNumber(arr){
  //code here  
  return Math.max.apply(null, arr);  
}
 
getMaxNumber(array) // should return 4