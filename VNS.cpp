#include <bits/stdc++.h>
#include <climits>
#include <string.h>

#define KMAX 2
using namespace std;
short int **tempsExecution;
/*{{26, 38, 27 ,88 ,95 ,55 ,54, 63, 23, 45, 86, 43, 43, 40, 37, 54, 35, 59, 43, 50},
 { 59 ,62, 44, 10, 23, 64, 47, 68, 54,  9, 30, 31, 92,  7, 14, 95, 76, 82, 91, 37},
 { 78, 90, 64, 49, 47, 20, 61, 93, 36, 47, 70, 54, 87, 13, 40, 34 ,55 ,13, 11,  5},
 { 88 ,54 ,47 ,83 ,84,  9 ,30 ,11 ,92 ,63 ,62, 75 ,48, 23, 85, 23,  4 ,31, 13, 98},
 { 69 ,30 ,61 ,35 ,53, 98, 94, 33, 77, 31, 54, 71, 78,  9, 79, 51, 76, 56, 80, 72}};*/
 short int **makeSpans;
int m,n;
int alea,ordre,LIMIT_SANS_AMELIORATION=5,strategie=0;

 short int maxi(short int a, short int b){
if(a > b ){
    return a;
}
return b;
}

short int makespan(short int liste[]){


makeSpans[0][0] = tempsExecution[0][liste[0]];
short int j,i;
for(j = 1 ; j < m ; j++){

        makeSpans[j][0] = makeSpans[j-1][0] + tempsExecution[j][liste[0]];
}

for(i = 1 ; i < n ; i++){
        makeSpans[0][i] = tempsExecution[0][liste[i]] + makeSpans[0][i-1];
        for(j = 1; j < m ; j++){

            makeSpans[j][i] = tempsExecution[j][liste[i]] + maxi(makeSpans[j-1][i],makeSpans[j][i-1]);
        }

}

return makeSpans[m-1][n-1];
}

void showSolution(short int  jobs[]){
for(short int i=0;i<n;i++) cout<< jobs[i]+1 << ",";

cout << makespan(jobs);
}

short int* swaper(short int jobs[], int i1, int i2){
  short int *res;
  short int tmp;
  res = new short int [n];
  memcpy(res,jobs,n*sizeof(short int));
  //showSolution(res);
  tmp = res[i2];
  res[i2] = res[i1];
  res[i1] = tmp;
  //showSolution(res);

    return res;
}



short int* permuter(short int jobs[],int i){
      short int *res,*tmp;
      res = new short int[n];
      memcpy(res,jobs,n*sizeof(short int));

for(int j=0;j<n;j++){
   tmp=swaper(res,i,j);
    if(makespan(tmp) < makespan(res)){
        if(strategie == 0)return tmp;
        else memcpy(res,tmp,n*sizeof(short int));

    }
    //tmp=swaper(tmp,i,j);
    delete[] tmp;

}
return res;

}



short int* decaler(short int jobs[],int job,int position){
  short int *res;
    res = new short int [n];
    short int tmp;
    tmp = jobs[position];
    int i=n-1;
    while (i > position){

        res[i] = jobs[i];

        i--;
    }
    res[i] = jobs[job];
    i--;
    res[i] = tmp;
    i--;
    while( job -1< i){
        res[i] = jobs[i+1];
        i--;
    }
    while(i>=0){
        res[i] = jobs[i];

        i--;
    }

  return res;

}

short int* Swap_localSearch(short int jobs[]){

      short int *res,*tmp;
      res = new short int[n];
      memcpy(res,jobs,n*sizeof(short int));

for(int i =0; i< n ; i++){
    tmp = permuter(res,i);
    //showSolution(tmp);
    if(makespan(tmp) < makespan(res))   memcpy(res,tmp,n*sizeof(short int));

    delete[] tmp;

}


return res;

}

short int* Deplacer(short int jobs[],int i){
      short int *res,*tmp;
      res = new short int[n];
        memcpy(res,jobs,n*sizeof(short int));
        tmp = new short int[n];
        memcpy(tmp,jobs,n*sizeof(short int));

      if(i != 0){
        //res = swaper(jobs,0,i);
        tmp[0] = res[i];
        for(int j=1; j <= i;j++)tmp[j] = res[j-1];
        for(int j=i+1; j < n;j++)tmp[j] = res[j];

        if(makespan(tmp) < makespan(res)) {if(strategie == 0 )return tmp;else memcpy(res,tmp,n*sizeof(short int));
 }

      }
      int l=1;
      while(l<n){

        if(i==l){
            if(l == n-1){
                return res;
            }
            delete[] tmp;

            tmp = swaper(res,l-1,l);
            l++;
        }
        delete[] tmp;
        tmp = swaper(res,l-1,l);
        if(makespan(tmp) < makespan(res)) {if(strategie == 0 )return tmp;else memcpy(res,tmp,n*sizeof(short int));};
        l++;
      }

return res;

}



short int* Shift_localSearch(short int jobs[]){

  short int *res,*tmp;
  //tmp = new short int[n];
  res = new short int[n];
  memcpy(res,jobs,n*sizeof(short int));
 // memcpy(tmp,res,n*sizeof(short int));

    for(int i = 0; i< n; i++){
       tmp = Deplacer(res,i);
       //showSolution(tmp);
       if(makespan(tmp) < makespan(res)){
         memcpy(res,tmp,n*sizeof(short int));
       }
    delete[] tmp;

    }
return res;
}


short int* shift(short int jobs[]){

  short int *res;
  int a=1,b=1;
    res = new short int [n];
    srand(time(0));
    while(a==b){
     a = rand()%n;
     b = rand()%n;
    }
    if(a<b){
       res = decaler(jobs,a,b);
    }
    else{
        res = decaler(jobs,b,a);

    }

return res;

}


short int* VNS(short int* solution_init){
int cpt_stagnation=0,stagnation,k;
short int* solution;
solution = new short int[n];
//generer une solution initiale
short int *solution_prod;
solution_prod = new short int[n];

//solution = solution_init;
 memcpy(solution,solution_init,n*sizeof(short int));

//solution_prod  = solution_init;
 memcpy(solution_prod,solution_init,n*sizeof(short int));

while(cpt_stagnation < LIMIT_SANS_AMELIORATION){
    stagnation = 1;
    k=1;

    while(k<KMAX){
            if(ordre == 0)
                        switch(k){
                            case 1:
                                solution = Swap_localSearch(solution);
                                break;

                            case 2:
                                solution = Shift_localSearch(solution);
                                break;

                        }
              else
                          switch(k){
                            case 2:
                                solution = Swap_localSearch(solution);
                                break;

                            case 1:
                                solution = Shift_localSearch(solution);
                                break;

                        }
         if(makespan(solution) < makespan(solution_prod))   {
            //solution_prod = solution;
              memcpy(solution_prod,solution,n*sizeof(short int));

            k = 1;
            stagnation = 0;

         }
        else {

            k++;
        }


    }//end while k

    if(stagnation == 1){
        //perturbation de la solution
        solution = shift(solution);
        cpt_stagnation++;
    }else{
        cpt_stagnation = 0;
    }

}

return solution_prod;
}
int main(int argv,char** args)
{

    if (argv <1) return -1;
        srand(time(0));

    short int *solution_init;
    short int* voisin;


        short int x, y;
  //tempsExecution = new int[10][20] ;
  ifstream in;
  in.open(args[1]);
    in >> m >> n;
  if (!in) {
    cout << "Cannot open file.\n";
    return 0;
  }
  alea = atoi(args[2]);

    solution_init = new short int [n];

  tempsExecution = new short int*[m];
  makeSpans =  new short int*[m];

  for (y = 0; y < m; y++) {
        tempsExecution[y] = new short int[n];
        makeSpans[y] = new short int[n];
    for (x = 0; x < n; x++) {
      in >> tempsExecution[y][x];



    }

  }

  in.close();

  if(alea == 0){
          int cpt =0;
          char delim[] = ",";
          char *ptr = strtok(args[3], delim);
          while (ptr != NULL && cpt < n){

                solution_init[cpt] = atoi(ptr)-1;
                cpt++;
                ptr = strtok(NULL, delim);


          }
          ordre = atoi(args[4]);
          LIMIT_SANS_AMELIORATION = atoi(args[5]);
          strategie = atoi(args[6]);

  }else{
          for(int u=0;u < n;u++){
            solution_init[u] = u;
          }
           for(int u=0;u < n;u++){
                  int a=1,b=1;
            while(a==b){
             a = rand()%n;
             b = rand()%n;
            }
           solution_init = swaper(solution_init,a,b);
          }
          ordre = atoi(args[3]);
          LIMIT_SANS_AMELIORATION = atoi(args[4]);
          strategie = atoi(args[5]);


  }
    voisin = VNS(solution_init);
    showSolution(voisin);
    return 0;
}
