import { removeDuplicates } from './solution';

describe('removeDuplicates', () => {
    it('should follow the expectation', () => {
        let nums: number[] = [1,1,2];
        let result: number = removeDuplicates(nums);

        let expectedNums: number[] = [1,2]
        expect(result).toEqual(2);
        for (let i = 0; i < result; i++) {
            expect(nums[i]).toEqual(expectedNums[i])
        }
    });

    it('should follow the expectation', () => {
        let nums: number[] = [0,0,1,1,1,2,2,3,3,4];
        let result: number = removeDuplicates(nums);

        let expectedNums: number[] = [0,1,2,3,4]
        expect(result).toEqual(5);
        for (let i = 0; i < result; i++) {
            expect(nums[i]).toEqual(expectedNums[i])
        }
    });
});
