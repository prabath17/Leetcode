# @param {Integer[]} arr
# @return {Integer}
def sum_odd_length_subarrays(arr)
    total=0
    for i in 0...arr.length
        for j in i...arr.length
            if (j-i+1).odd?
                subarr=arr[i..j]
                total +=subarr.sum
            end
        end
    end
    return total

end