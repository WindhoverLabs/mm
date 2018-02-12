#ifndef MATRIX1F10_HPP
#define MATRIX1F10_HPP


#include "cfe.h"
#include "Vector10F.hpp"
#include "Matrix10F10.hpp"
#include "Matrix10F1.hpp"

namespace math
{

/* Forward declare 10F1 */
class Matrix10F1;

class Matrix1F10
{
private:
    static const int SIZE = 1;
    Vector10F data[SIZE];
    Vector10F nan;

public:
    Matrix1F10();
    Matrix1F10(Vector10F m0);
    ~Matrix1F10();
    Vector10F& operator [] (uint32 i);
    Vector10F operator [] (uint32 i) const;
    Matrix1F10 operator*(const Matrix10F10 &matIn);
    Matrix10F1 Transpose(void);
    void Zero(void);

protected:

};

}

#endif
