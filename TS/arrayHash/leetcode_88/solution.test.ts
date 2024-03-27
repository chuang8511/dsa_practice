import { merge } from './solution';

describe('merge function', () => {
    it('should merge two sorted arrays into one sorted array', () => {
        let nums1: number[] = [1, 2, 3, 0, 0, 0];
        let m: number = 3;
        let nums2: number[] = [2, 5, 6];
        let n: number = 3;

        merge(nums1, m, nums2, n);

        expect(nums1).toEqual([1, 2, 2, 3, 5, 6]);
    });
});
