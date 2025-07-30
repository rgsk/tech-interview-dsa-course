function merge(arr: number[], start: number, mid: number, end: number): void {
    const aux: number[] = [];
    let i = start;
    let j = mid + 1;

    while (i <= mid && j <= end) {
        if (arr[i] < arr[j]) {
            aux.push(arr[i]);
            i++;
        } else {
            aux.push(arr[j]);
            j++;
        }
    }

    while (i <= mid) {
        aux.push(arr[i]);
        i++;
    }

    while (j <= end) {
        aux.push(arr[j]);
        j++;
    }

    for (let k = 0; k < aux.length; k++) {
        arr[start + k] = aux[k];
    }
}

function mergeSort(arr: number[], start: number, end: number): void {
    if (start < end) {
        const mid = Math.floor((start + end) / 2);
        mergeSort(arr, start, mid);
        mergeSort(arr, mid + 1, end);
        merge(arr, start, mid, end);
    }
}

function sortArray(nums: number[]): number[] {
    mergeSort(nums, 0, nums.length - 1);
    return nums;
}

// tests-start
const nums = [5, 2, 3, 1];
console.log(sortArray(nums));
// tests-end
