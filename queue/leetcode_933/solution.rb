class RecentCounter
    def initialize()
        @ping = []
    end


=begin
    :type t: Integer
    :rtype: Integer
=end
    def ping(t)
        @ping.append(t)
        while t - @ping[0] > 3000
            @ping.shift
        end

        return @ping.length
    end


end

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter.new()
test_cases = [1, 100, 3001, 3002]
for test_case in test_cases
    print(obj.ping(test_case), "\n")
end