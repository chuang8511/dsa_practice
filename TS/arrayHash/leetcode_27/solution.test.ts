import { removeElement } from './solution';
import 'jest-extended';

describe('removeElement function', () => {

    it('should follow the test result', () => {
        let nums: number[] = [3,2,2,3];
        let val: number = 3;
        const k: number = removeElement(nums, val);

        expect(nums).toEqual([2,2]);
        expect(k).toEqual(2);
    });

    it('should follow the test result', () => {
        let nums: number[] = [0,1,2,2,3,0,4,2];
        let val: number = 2;
        const k: number = removeElement(nums, val);

        expect(nums).toIncludeAllMembers([0,1,4,0,3]);
        expect(k).toEqual(5);
    });
});
