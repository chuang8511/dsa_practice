export function removeElement(nums: number[], val: number): number {
    let k = nums.length
    
    for (let i = nums.length - 1; i >= 0 ;i--) {
        if (nums[i] == val && i == nums.length - 1) {
            nums.pop()
            k--
            continue
        }
        if (nums[i] == val) {
            const replaceNumber = nums.pop() as number
            nums[i] = replaceNumber
            k--
        }
    }
    return k    
};