// Learning
// [...Array(n).keys()].map(i => i+1);
// Array.filter((ele) => condition )
// [...currentArray] -> copy of currentArray
export function combine(n: number, k: number): number[][] {

    let remainingNums: number[] = [...Array(n).keys()].map(i => i+1);
    let res: number[][] = []

    backtrace(remainingNums, k, [], res)

    return res
};

function backtrace(remainingNums: number[], remainingCount: number, currentArray: number[], res: number[][]): void {
    for (var num of remainingNums) {
        let copyNums: number[] = remainingNums.filter((ele) => ele > num);
        currentArray.push(num)
        remainingCount--
        if (remainingCount != 0) {
            backtrace(copyNums, remainingCount, currentArray, res);
        } else {
            res.push([...currentArray])
            
        }
        currentArray.pop()
        remainingCount++
    }
}