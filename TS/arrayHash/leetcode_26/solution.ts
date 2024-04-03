export function removeDuplicates(nums: number[]): number {
    if (nums.length == 1) return 1

    let k: number = 1;
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i-1]) {
            nums[k] = nums[i];
            k++;
        }
    }
    return k
};