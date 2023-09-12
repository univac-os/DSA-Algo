/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    nums.sort((a,b)=>{
        let n1=a.toString()
        let n2=b.toString()
        return parseInt(n1+n2) > parseInt(n2+n1) ? -1 : 1
    })
    if (nums[0]===0) return '0'
    return nums.join('')
};