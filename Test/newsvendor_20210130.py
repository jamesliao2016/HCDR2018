import random
import numpy as np

def produceDemand(x):
    return random.randint(2,20)

def devideDemand(x,y0,y1):
    [res0, res1] = [0,0]
    if (y0>0) and (y1>0):
        tmp_ratio = y0/(y0+y1)
        res0 = int(tmp_ratio*x)
        res1 = x - res0
    elif (y0==0) and (y1>0):
        res1 = x
    elif (y0>0) and (y1==0):
        res0 = x
    return [res0,res1]

def robotReplenish(x,nums):
    if (not nums):
        return min(1,x)
    tmp_median = np.median(nums)
    return min(int(tmp_median/2), x)


def computeRevenue(x,y,z):
    # x: current revenue
    # y: allocation
    # z: demand
    tmp_stock = min(x,y)
    tmp = min(z,tmp_stock)*2
    return max(x-y+tmp-1,0)

# for ii in range(5):
#     zz = input(str(ii)+"input: ")
#     print(zz)


if __name__ == '__main__':
    val0 = 10
    print("start money is: ", val0)
    expect_max = 10

    val_robot = 10
    stock_robot = 0

    list_demand = []

    # game period
    val_game_period = 30

    for ii in range(val_game_period):
        print("*** round ", (ii+1))
        print("max allocation is: ", val0)

        # initial stock level is 0
        zz=0

        # replenish the stock if current money is positive
        if val0>0:
            zz = input(" input: ")

        # compute the inventory replenishment of the robot player
        stock_robot = robotReplenish(val_robot,list_demand)

        # get the demand of current phase
        current_demand = produceDemand(ii)

        # generate the demand list
        list_demand.append(current_demand)

        # divide the demand into two streams
        tmp_demand, robot_demand = devideDemand(current_demand,val0,val_robot)

        # get the ideal revenue
        expect_max+= (tmp_demand-1)

        # compute the revenue of human player
        val0 = computeRevenue(val0,int(zz) ,tmp_demand)

        # compute the revenue of the robot player
        val_robot = computeRevenue(val_robot,stock_robot,robot_demand)

        print("** demand: ",current_demand, ", current revenue: ", val0, ", robot revenue: ",val_robot)
        if val0 == 0:
            print("game over")
            # break

    print("------------- result ------------- ")
    print("final revenue: ",val0)
    print("max expected revenue: ",expect_max)
