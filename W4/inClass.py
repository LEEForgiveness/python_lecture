{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "history_visible": true,
      "authorship_tag": "ABX9TyOlZCMvgAKTqClMxdaKYeRY",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/LEEForgiveness/python_lecture/blob/main/W4/inClass.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "qmsgZy_usgBv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "650911f9-e45c-4f6c-fff5-966e25e71ffa"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x의 평균 값: 5.0\n",
            "y의 평균 값: 90.5\n"
          ]
        }
      ],
      "source": [
        "import numpy as np\n",
        "\n",
        "x = np.array([2, 4, 6, 8])\n",
        "mx = np.mean(x)\n",
        "y = np.array([81, 93, 91, 97])\n",
        "my = np.mean(y)\n",
        "print(\"x의 평균 값: %.1f\" % mx)\n",
        "print(\"y의 평균 값: %.1f\" % my)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def dividend_sol(mx, my, x, y):\n",
        "  d = 0\n",
        "  for i in range(len(x)):\n",
        "    d += (x[i] - mx) * (y[i] - my)\n",
        "  return d\n",
        "\n",
        "divisor = sum([(i - mx)**2 for i in x])\n",
        "dividend = dividend_sol(mx, my, x, y)\n",
        "\n",
        "a = dividend / divisor\n",
        "\n",
        "b = my - (mx*a)\n",
        "\n",
        "print(\"분모: %.1f\" % divisor)\n",
        "print(\"분자: %.1f\" % dividend)\n",
        "print(\"기울기 a: %.1f\" % a)\n",
        "print(\"y 절편 b: %.1f\" % b)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5Nlrano29DqC",
        "outputId": "8146c8fe-954f-4cb0-e762-b2cb65c9b194"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "분모: 20.0\n",
            "분자: 46.0\n",
            "기울기 a: 2.3\n",
            "y 절편 b: 79.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def predict(x):\n",
        "  fake_a = 3\n",
        "  fake_b = 76\n",
        "  prediction = fake_a * x + fake_b\n",
        "  return prediction\n",
        "\n",
        "def mse(y, y_pred):\n",
        "  mse_result = 0\n",
        "  hap = 0\n",
        "  for i in range(len(y)):\n",
        "    hap += (y[i] - y_pred[i])**2\n",
        "  mse_result = hap / len(y)\n",
        "  return mse_result\n",
        "\n",
        "predict_result = []\n",
        "for i in range(len(x)):\n",
        "  print(\"공부시간=%d\" %x[i], end = ' ')\n",
        "  print(\"실제점수=%d\" %y[i], end = ' ')\n",
        "  predict_result.append(predict(x[i]))\n",
        "  print(\"실제점수=%d\" %predict_result[i])\n",
        "mse_result = mse(y, predict_result)\n",
        "print(\"평균 제곱 오차: %.1f\" % mse_result)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Cqwx4XGw-_x_",
        "outputId": "a5a8777e-ff10-4fed-8b2c-5b63e4811037"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "공부시간=2 실제점수=81 실제점수=82\n",
            "공부시간=4 실제점수=93 실제점수=88\n",
            "공부시간=6 실제점수=91 실제점수=94\n",
            "공부시간=8 실제점수=97 실제점수=100\n",
            "평균 제곱 오차: 11.0\n"
          ]
        }
      ]
    }
  ]
}