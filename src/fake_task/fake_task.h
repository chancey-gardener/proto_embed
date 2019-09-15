#ifndef FAKE_TASK_H
#define FAKE_TASK_H
#include <vector>
#include <Eigen/Dense>
#include <random>

using namespace std;

const int DIM = 300;
class LinearNeuron {
public:
    LinearNeuron(int num_inputs, double weight);
    double output(vector<double> input_vals);


private:
    int num_inputs;
    double weight;
    void weight_init();
  vector<double> input_weights;
};

vector<vector<double>> getHidden(vector<vector<double>>cprobs,
                                 int schidx,
                                 int hidden_size);

 class NnLayer {
 public:
     NnLayer(int dims);
     vector<double> OutPut(NnLayer input);
 private:
     default_random_engine weight_init_gen;
     vector<double> weights;
     vector<LinearNeuron> values;
     vector<double>weight_vector_init(int len);
     double weight_init();
     uniform_real_distribution<double> init_dist;
     double bias;
 };


#endif