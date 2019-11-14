import numpy as np

class neural_network:
    def train_model(self,input_x,input_y):

    def predict_value(self,input_x):
        value_res = input_x
        return value_res

def forward_probagation(input_x,input_y,weight1,weight2,b0,b1):
    for val_x in input_x:
        for val_weight in weight1:
            tmp = np.array(val_x).dot(np.array(val_weight))


if __name__ == '__main__':
    input_x = [[1,1],
               [1,3],
               [2,4],
               [3,3],
               [3,2],
               [3,1]
               ]
    input_y = [0,
               1,
               1,
               1,
               0,
               0]
    # weight1 = [[[1,2],[1,2],[1,2]],
    #            [[1,2],[1,2],[1,2]]]
    weight1 = [[1,2],[1,2],[1,2]]

    weight2 = [[1,2],
               [2,3],
               [3,4]]
    b0 = 0
    b1 = 1
    # print(neural_network.predict_value(input_x))