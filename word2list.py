{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPnXQdIZNnMolG1UF0iB0Wm",
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
        "<a href=\"https://colab.research.google.com/github/Aromie/Python/blob/master/word2list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "_5G3XGi4B1ru",
        "outputId": "9f07091b-d065-4c57-868c-9f31f4121335"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'start'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 2
        }
      ],
      "source": [
        "word='start'\n",
        "word\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#word='start'\n",
        "end_letter=''\n",
        "word2list = []\n",
        "word2list = list(word)\n",
        "end_letter=word2list[-1:]\n",
        "end_letter"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Azs_xs4SMMx0",
        "outputId": "cc452eca-5135-4512-b5a9-8df264826429"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "['t']"
            ]
          },
          "metadata": {},
          "execution_count": 15
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#단어에서 끝 알파벳을 추출하는 함수\n",
        "def check_end_letter(word):\n",
        "  word2list = []\n",
        "  word2list = list(word)\n",
        "  end_letter=''\n",
        "  end_letter=word2list[-1:]\n",
        "  return end_letter\n"
      ],
      "metadata": {
        "id": "BGBp_ofXCFQW"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "check_end_letter(word)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "jmUHqgr1CzzE",
        "outputId": "6a520df9-6733-4d00-d632-fbf05c91438c"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'start'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "check_end_letter(word)"
      ],
      "metadata": {
        "id": "UbH2--GFCM7T"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}