/**
 * @param {string} s
 * @return {string}
 */
var greatestLetter = function(s) {
    const map = new Map();
    let greatest = '';
    for(let i=0; i< s.length;i++){
        const key = s[i].toLowerCase();
        if(!map.has(key)){
            map.set(key, {l: s[i] === key, h: s[i] === key})
        } else {
            // if key exist 
            // check if it has lower or upper , if we get alternate update greatest 
            const existingValue = map.get(key);
            if(existingValue.l){//key is lowercase
                if(s[i] !== key){
                    if(greatest < s[i].toUpperCase()){
                        greatest = s[i].toUpperCase();
                    }
                }
            } else {
                // already high
                if(s[i] === key){ 
                    if(greatest < s[i].toUpperCase()){
                        greatest = s[i].toUpperCase();
                    }
                }
            }
        }
    }
    return greatest ?? -1;
};