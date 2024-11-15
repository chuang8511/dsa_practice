class MinStack
    def initialize()
        # [val, min]
        @stack = []
    end


=begin
    :type val: Integer
    :rtype: Void
=end
    def push(val)
        top = @stack.last
        if top
            min = top[1]
            @stack.append([val, [min, val].min])
        else
            @stack.append([val, val])
        end
    end


=begin
    :rtype: Void
=end
    def pop()
        top = @stack.last
        if top
            @stack.pop()
        else
            return nil
        end
    end


=begin
    :rtype: Integer
=end
    def top()
        top = @stack.last
        if top
            top[0]
        else
            return nil
        end
    end


=begin
    :rtype: Integer
=end
    def get_min()
        top = @stack.last
        if top
            top[1]
        else
            return nil
        end
    end


end
