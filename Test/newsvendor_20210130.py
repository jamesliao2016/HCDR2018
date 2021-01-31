import random

def produceDemand(x):
    return random.randint(0,10)

def computeRevenue(x,y,z):
    # x: current revenue
    # y: allocation
    # z: demand
    tmp = min(z,y)*2
    return x-y+tmp-1

# for ii in range(5):
#     zz = input(str(ii)+"input: ")
#     print(zz)

if __name__ == '__main__':
    val0 = 10
    print("start money is: ", val0)
    expect_max = 10

    for ii in range(10):
        print("*** round ", (ii+1))
        print("max allocation is: ", val0)
        zz = input(" input: ")
        tmp_demand = produceDemand(ii)
        expect_max+= (tmp_demand-1)
        val0 = computeRevenue(val0,int(zz) ,tmp_demand)
        print("** demand: ",tmp_demand, ", current revenue: ", val0)
        if val0 == 0:
            print("game over")
            break

    print("------------- result ------------- ")
    print("final revenue: ",val0)
    print("max expected revenue: ",expect_max)
