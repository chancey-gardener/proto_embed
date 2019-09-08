#ifndef FAKE_TASK_H
#define FAKE_TASK_H
#include

class LinearNeuron {
    private:
        vector<double> input_weights;

public:
    double output(vector<double> input_vals);

}

vector<vector<double>> getHidden(vector<vector<double>> cprobs);

#endif