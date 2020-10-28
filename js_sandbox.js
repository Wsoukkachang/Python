const array = [1,2,4];
 
function getMaxNumber(arr){
  //code here  
  return Math.max.apply(null, arr);  
}
 
getMaxNumber(array) // should return 4

const character = {
  name: 'Simon',
  getCharacter() {
    return this.name;
  }
};
const giveMeTheCharacterNOW = character.getCharacter.bind(character);
 
//How Would you fix this?
console.log('?', giveMeTheCharacterNOW()); //this should return 'Simon' but doesn't
