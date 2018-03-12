import numpy
def f1(a):
    rotate=24*numpy.random.rand(1)
    if rotate< 1:
        return a
    elif rotate< 2:
        return a[::-1,:,:].transpose(0,2,1)
    elif rotate< 3:
        return a[::-1,:,:].transpose(1,0,2)
    elif rotate< 4:
        return a[::-1,:,:].transpose(2,1,0)
    elif rotate< 5:
        return a[:,::-1,:].transpose(2,1,0)
    elif rotate< 6:
        return a[:,::-1,:].transpose(1,0,2)
    elif rotate< 7:
        return a[:,::-1,:].transpose(0,2,1)
    elif rotate< 8:
        return a[:,:,::-1].transpose(0,2,1)
    elif rotate< 9:
        return a[:,:,::-1].transpose(1,0,2)
    elif rotate<10:
        return a[:,:,::-1].transpose(2,1,0)
    elif rotate<11:
        return a.transpose(2,0,1)
    elif rotate<12:
        return a.transpose(1,2,0)
    elif rotate<13:
        return a[::-1,::-1,:]
    elif rotate<14:
        return a[::-1,:,::-1]
    elif rotate<15:
        return a[:,::-1,::-1]
    elif rotate<16:
        return a[:,::-1,::-1].transpose(1,2,0)
    elif rotate<17:
        return a[:,::-1,::-1].transpose(2,0,1)
    elif rotate<18:
        return a[::-1,:,::-1].transpose(1,2,0)
    elif rotate<19:
        return a[::-1,:,::-1].transpose(2,0,1)
    elif rotate<20:
        return a[::-1,::-1,:].transpose(1,2,0)
    elif rotate<21:
        return a[::-1,::-1,:].transpose(2,0,1)
    elif rotate<22:
        return a[::-1,::-1,::-1].transpose(1,0,2)
    elif rotate<23:
        return a[::-1,::-1,::-1].transpose(2,1,0)
    elif rotate<24:
        return a[::-1,::-1,::-1].transpose(0,2,1)
def f2(a):
    return 24*numpy.random.rand(1)*a