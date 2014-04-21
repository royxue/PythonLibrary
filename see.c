#include <stdio.h>

struct person
{
	char name[32];
	int age;
	float weight
};

struct person p[1];

void main()
{
	FILE *fp;
	int i;
	fp = fopen("test.bin","rb");
	fread(p, sizeof(struct person), 2, fp);
	fclose(fp);
	printf("%s %d %f\n", p[0].name, p[0].age, p[0].weight);

}
