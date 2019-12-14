//
//  main.c
//  hw3
//
//  Created by Ali Arda İsenkul on 26.05.2019.
//  Copyright © 2019 Ali Arda İsenkul. All rights reserved.
//


#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

void fCurrent(char* inp, int *currentChar,const int son, int degree, int *fChar);
void findquadrant(char* inp, int degree, int *fChar);
void fDegree(char* inp, int *currentChar,int degree, int *mDegree);
int creak(char *inp, int **currentChar, char** arr, int maxDegree);
char *trim(char *str);//I get it from the internet: https://stackoverflow.com/questions/122616/how-do-i-trim-leading-trailing-whitespace-in-a-standard-way
void changeInput(char* trinp, char** arr, const int maxDegree, int *Degree, int row, int column, int *kepp);

int main(){
    char inp[350];
    char trinp[350];
    char ninput[500];
    int mDegree = 0;
    int currentC = 0;
    int empty = 0;
    int maxDegree = 0;
    int Degree = 0;
    int col = 0;
    int row = 0;
    int fDeg =0;
    scanf("%s",inp);
    if(inp[0]!='+'){
        for(int i = 0;i<strlen(inp);i++){
            strcpy(trinp,trim(inp));
            printf("%c\n",trinp[i]);
        }
        exit(0);
    }
    strcpy(trinp,trim(inp));
    fDegree(trinp, &currentC, 0, &mDegree);
    currentC = 0;
    for(int i = 0; i<strlen(trinp); i++){
        if(trinp[i] == '+')
            continue;
        currentC=0;
        fCurrent(trinp, &currentC, i,0, &fDeg);
        
        int dif = mDegree - fDeg;
        if(dif){
            strncpy(ninput,trinp,i);
            ninput[i] = '+';
            for(int j = 1;j<5;j++){
                ninput[i+j] = trinp[i];
            }
            ninput[i+5] = '\0';
            for(int from=i+1;from<strlen(trinp);from++){
                ninput[from+4]=trinp[from];
                ninput[from+5] ='\0';
            }
            strcpy(trinp,ninput);
            trinp[strlen(trinp)] = '\0';
        }
    }
    fDegree(inp, &empty, 0, &maxDegree);
    row = (int) pow(2.0,(double)maxDegree);
    col = (int) pow(2.0,(double)maxDegree);
    char **arr = (char**) malloc(row * sizeof(char*));
    
    for (int i = 0; i < row; i++ )
    {
        arr[i] = (char*) malloc(col * sizeof(char));
        for(int j=0;j<col;j++)
            arr[i][j]='#';
        arr[i][col]='\0';
    }
    empty = 0;
    changeInput(trinp, arr, maxDegree, &Degree, 0, 0, &empty);

    for (int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            printf("%c",arr[i][j]);
        }
        printf("\n");
    }
    for(int i=0;i<row;i++){
        free(arr[i]);
    }
    free(arr);
}

int creak(char *inp, int **currentChar, char** arr, int maxDegree){
    
    for(int i = 0 ; i < strlen(inp) ; i++){
        for(int j = 0 ; j < strlen(inp) ; j++){
            printf("%c", arr[i][j]);
        }puts("");
        
        
}
    return maxDegree;
}

void changeInput(char* trinp, char** arr, const int maxDegree, int *Degree, int row, int column, int *kepp){
    int imm = 0;
    if(*kepp == 0 && trinp[*kepp] == '+'){
        (*kepp)++;
    }
    
    while(imm < 4){
       
        switch (imm) {
            case 0:
                
                break;
            case 1:
                column += (int)(pow(2.0,(double)(maxDegree-(*Degree)))/2);
                break;
            case 2:
                 row += (int) (pow(2.0,(double)(maxDegree - (*Degree)))/2);
                break;
            case 3:
                column -= (int) (pow(2.0,(double)(maxDegree - (*Degree)))/2);
                break;
        }
      
        imm++;
        int myArray[5] = {maxDegree,*Degree,row,column,*kepp};
        
        while (myArray[0] -myArray[1] >0 ){
            myArray[2] =myArray[0]*myArray[1];
            myArray[3] =myArray[0]*myArray[1];
            myArray[1]++;
        }
        if(trinp[*kepp] == '+'){
            (*Degree)++;
            (*kepp)++;
            changeInput(trinp,arr,maxDegree,Degree,row,column,kepp);
        }
        else{
            arr[row][column] = trinp[*kepp];
            (*kepp)++;
        }
    }
    (*Degree)--;
}
void fCurrent(char* inp, int *currentChar,const int son, int degree, int *fChar){
    
    if(*currentChar > strlen(inp)){
        return;
    }
    if((*currentChar) == 0 && inp[(*currentChar)] == '+'){
        (*currentChar)++;
        degree++;
    }
    int dep = 0;
    for(;dep <4; dep++){
        if((*currentChar) == son){
            (*fChar) = degree;
        }
        if(inp[(*currentChar)++] == '+'){
            fCurrent(inp,currentChar,son,degree+1,fChar);
        }
    }
}
void findquadrant(char* inp, int degree, int *fChar){
   
    char  input[256];
    //printf("Enter the input\n");
     
    scanf("%s" , input);
    
    if(strlen(input)<5){
        printf("%s\n",input);
        exit(0);
    }
    // printf("The pattern is %s\n",input);
    int def =strlen(input);
}


void fDegree(char* inp, int *currentChar,int degree, int *mDegree){
    int deger = 1;
    int deg = 0;
    
    if(inp[(*currentChar)]=='+'&& (*currentChar)==0){
        (*currentChar)++;
        deger = *currentChar + degree;
        degree++;
    }
    for (int u = 0;u<strlen(inp);u++){
        continue;
        
        
    }
    while(deg!=4){
        if((*mDegree) < degree){
            (*mDegree) = degree;
            deger++;
        }
        if(inp[(*currentChar)++]=='+'){
            deger++;
            fDegree(inp,currentChar,degree+1,mDegree);
        }
        deg++;
        deger = 0;
    }
}
    
char *trim(char *str)
{
    char *end;
    while(isspace((unsigned char)*str)) str++;
    if(*str == 0)
        return str;
    end = str + strlen(str) - 1;
    while(end > str && isspace((unsigned char)*end)) end--;
    end[1] = '\0';
    return str;
}



