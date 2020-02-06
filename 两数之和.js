// O(n^2)
function func(arr, target) {
    for (var i = 0; i < arr.length; i++) {
        for (var j = i + 1; j < arr.length; j++) {
            if (arr[i] + arr[j] === target) {
                return [i, j];
            }
        }
    }
    return null;
}

var nums = [2, 7, 11, 15];
var target = 9;
var res = func(nums, target);

console.log(res);