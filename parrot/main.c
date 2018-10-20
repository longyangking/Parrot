#include "phrase.h"
#include "stdio.h"
#include "string.h"
#include "unistd.h"
#include "getopt.h"

char *__help_info__ = "Parrot help information";

int main(int argc, char *argv[]){
    int opt;
    char *optstring = "f:hv";
    const struct option long_options[] = {
        {"filename", required_argument, NULL, 'f'},
        {"help", no_argument, NULL, 'h'},
        {"verbose", no_argument, NULL, 'v'},
        {NULL, 0, NULL, 0}
    };

    char *filename;
    int verbose = 0;
    while((opt = getopt_long(argc, argv, optstring, long_options, NULL))!=-1){
        switch(opt){
            case 0: break;
            case 'h': 
                printf("%s\n",__help_info__);
                break;
            case 'f': 
                filename = optarg;
                break;
            case 'v': 
                verbose = 1;
                break;
            default:
                printf("Unknown parameters: %s\n", opt);
                return 0;
        }
    };

    if (verbose) {
        printf("Filename: %s\n", filename);
    };

    return 0;
    // if (argc > 2) {
    //     printf("Error: Too many arguments!\n");
    //     return;
    // }
}