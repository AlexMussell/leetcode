const numJewelsInStones = (J, S) => {
    if (!J || !S) return 0;
    
    let count = 0;
    for (const c of S) {
        if (J.includes(c)) count++;
    }
    
    return count;
};