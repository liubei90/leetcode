/*
 * @lc app=leetcode.cn id=9 lang=javascript
 *
 * [9] 回文数
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    /* 
    var strx = String(x);
    var restrx = '';
    for (var i = strx.length - 1; i >= 0; i--) {
        restrx += strx.charAt(i);
    }
    // 1. 直接比较字符串 2. 循环比较每个数组的值
    return restrx === strx;
    */

    if (x < 0 || (x % 10 === 0 && x !== 0)) {
        return false;
    }

    var res = 0;
    while (x > res) {
        res = res * 10 + x % 10;
        x = Math.floor(x / 10);
    }
    return x === res || x === Math.floor(res / 10);
};
// @lc code=end

[121, -121, 10].forEach(num => {
    console.log(num, isPalindrome(num));
});