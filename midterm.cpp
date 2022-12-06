double s = 0;

int count ( int n){
    int x[2][3][2] = { { { 0, 1 }, { 2, 3 }, { 4, 5 } },
                       { { 6, 7 }, { 8, 9 }, { 10, 11 } } };

    for (int i=0; i<n; i++)
{
	for(int j=1; j<n; j*=2)
	{
		if(j<i)
		{
			for(int k=j; k<n; k*=4)
			{
				s += x[i][j][k];
			}
		}
	}
}
    return s;
}

int main(){
    int n = 5;

    count(n);
}

