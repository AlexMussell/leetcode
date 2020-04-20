const isPalindrome = x => {
    if (x < 0 || (x % 10 === 0 && x !==0)) {
        return false
    }
    
    let reverse = 0;
    let j = x;
    
    while (j > 0){
        reverse = (reverse * 10) + (j % 10);
        j = ~~(j/10)
    }
    
    return x === reverse;
    
};