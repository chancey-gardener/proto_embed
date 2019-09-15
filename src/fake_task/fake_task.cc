#include <Eigen/Dense>
#include <vector>
#include <algorithm>
#include <random>
#include <cmath>
#include "/home/chanceygardener/repos/proto_embed/src/utils/utils.h"
#include "fake_task.h"


using namespace std;
using namespace Eigen;





LinearNeuron::
LinearNeuron(int num_inputs, double weight) {
    // initiate weights at random values (uniform dist for now)
    //
    vector<double> imps = weight_init(num_inputs);
    this->input_weights = imps;

}

    double LinearNeuron::output(vector<LinearNeuron> input_vals) {
         double out = 0;

        return out;

 }


    // TODO( maybe just have this compute for the nonzero value rather than fucking iterate...
    // TODO( <continued> since it's a 1-hot vector going through this fucker.
    vector<vector<double>>
        getHidden(vector<vector<double>> cprobs, int schidx, int hidden_size) {
        double num_inputs = cprobs.size();
        vector<int> n_hot_in = vector<int>(num_inputs, 0);
        n_hot_in[schidx] = 1;
        vector<LinearNeuron> hidden;
        for (int i = 0; i < hidden_size; i++) {
            LinearNeuron hnode = LinearNeuron(num_inputs);
            hidden[i] = hnode;
    }


}
NnLayer::NnLayer(int dims) {
    uniform_real_distribution<double> init_dist(0.0, 1.0);
    vector<double> weights = weight_vector_init(dims);
}

vector<double> NnLayer::OutPut(NnLayer input) {
    vector<double> out = vector<double>();
    for (int i = 0; i < input.values.size(); i++ ) {
        double weight = input.values[i].weight;
        double ival = input.vals[i].value;
        double prod = weight * ival;
        out += prod;
    }



    return out;
}

double NnLayer::weight_init() {
    return init_dist(weight_init_gen);
}

vector<double>
NnLayer::weight_vector_init(int len) {

    vector<double> out;
    for (int i = 0; i < len; i++ ) {
        out[i] = weight_init();
    }
    return out;
}
