// Matcher doc: https://jestjs.io/docs/expect#tocontainequalitem
import { combine } from './solution';

describe('combine', () => {
    it('should follow the expectation', () => {
        let result: number[][] = combine(4,2);

        let expectedNums: number[][] = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        for (let i = 0; i < result.length; i++) {
            console.log(result)
            expect(expectedNums).toContainEqual(result[i])
        }
    });

    it('should follow the expectation', () => {
        let result: number[][] = combine(1,1);

        let expectedNums: number[][] = [[1]]
        for (let i = 0; i < result.length; i++) {
            console.log(result)
            expect(expectedNums).toContainEqual(result[i])
        }
    });
});
