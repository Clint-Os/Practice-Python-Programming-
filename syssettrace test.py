def func(x=10, y=10):
    return x*y

def func2(x,y=10):
    y=func(x,y)
    return x*y #this is a local variable

if __name__ == '__main__':
    import sys
    def tracer(frame,event,arg): 
        if event == 'line':
            filename, lineno = frame.f_code.co_filename, frame.f_lineno #get the filename and line number
            print(filename, end='\t')
            print(frame.f_code.co_name, end='\t') #get the function name
            print(lineno, end='\t') #get the line number in the filename 
            print(frame.f_locals, end='\t')
            argnames = frame.f_code.co_varnames[:frame.f_code.co_argcount]
            print('arguments:', end = '\t')
            print(str.join(', ', [
                '%s=%r' % (argname, frame.f_locals[argname]) for argname in argnames
            ])) #get the argument names and values 
        return tracer #pass function along for next time 
    

sys.settrace(tracer)
func(10,30)
func(20,30)
func2(33) 

