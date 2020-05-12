const kidsWithCandies = (candies, extra) => {
    let max = Math.max(...candies);
    return candies.map(x => x + extra >= max);
};

        