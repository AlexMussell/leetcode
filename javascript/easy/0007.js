const reverse = x => {
  const INT32_MAX = Math.pow(2, 31) -1;
  const INT32_MAX_DIV_10 = INT32_MAX / 10

  const sign = x < 0 ? -1 : 1;

  let result = 0;
  let abs_result = Math.abs(x)

  while (abs_result > 0) {
    if (result > INT32_MAX || (result == INT32_MAX_DIV_10 && remainder > 7)){
        return 0
    }
     
    result = (result * 10) + (abs_result % 10);
    abs_result = Math.floor(abs_result / 10);
  };

  return result * sign
};

reverse(123);
