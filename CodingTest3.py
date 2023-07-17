def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, (len(nums))):
            for k in range(j+1, (len(nums))):
                addition = nums[i] + nums[j] + nums[k] # addition
                if isPrime(addition):
                    answer += 1

    return answer


# Detector to detect Prime Number
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:  # if the reminder is 0, return false
            return False

    return True # if 0 is not reminder, return true. because it is prime number.



if __name__ == '__main__':
    num_list = [1, 2, 3, 4]
    num_list2 = [1,2,7,6,4]
    print(solution(num_list))
    print(solution(num_list2))