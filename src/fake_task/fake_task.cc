#include <eigen3>
#include <vector>
#include <algorithm>
#include <random>
#include <cmath>
#include "/home/chanceygardener/repos/proto_embed/src/utils/utils.h"

using namespace std;

vector<double>
weight_init(int len) {
    vector<double> out;
    default_random_engine gen;
    uniform_real_distribution<double> rdist(0, 1);
    for (int i = 0; i < len; i++ ) {
        out[i] = rdist(gen);
    }
    return out;
}

 LinearNeuron::LinearNeuron(int n_inputs) {
    // initiate weights at random values (uniform dist for now)
    //
     this->input_weights = weight_init(n_inputs);
 }

    double LinearNeuron::output(vector<double> input_vals) {
         double out = 0;
        for (int i = 0; i < input_weights.size(); i++ ) {
            double weight = this->input_weights[i];
            double ival = input_val;
            double prod = weight * ival;
            double += prod;
     }
        return out

 }


// TODO( maybe just have this compute for the nonzero value rather than fucking iterate...
// TODO( <continued> since it's a 1-hot vector going through this fucker.
vector<vector<double>>
    getHidden(vector<vector<double>> cprobs, int schidx, int size) {
    vector<int> n_hot_in = vector<int>(size, 0);
    n_hot_in[schidx] = 1;
    vector<LinearNeuron<cprobs.size()>>(size) hidden = weight_init(size);
    for (node: hidden) {
        double oval = node.output(n_hot_in);
    }




}