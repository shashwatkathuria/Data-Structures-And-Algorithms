#include<iostream>
#include<fstream>
#include<string.h>
#include<bits/stdc++.h>

using namespace std;

bool randomInputGenerator(int n);

struct node
{
    bool is_word;
    struct node *children[27];
};

class Trie
{
    public:
        int j;
        node *root;
        Trie()
        {
            j = 1;
            root = NULL;
        }
        bool searchWord(const char *word);
        bool load();
        unsigned int size();
        bool printNodes();
        void freeNode(node *currentNode);
        bool insertNewWord(const char *word);
        bool deleteWord(const char *word);

};

int main(void)
{
    Trie trie_1;
    int choice = 0;
    char tosearch[45];
    char toinsert[45];
    char todelete[45];
    bool flag2;
    int n;
    cout<<endl<<"------------------------------------------------------"<<endl;
    cout<<endl<<"Enter how many random words you want : ";
    cin>>n;
    cout<<endl;
    cout<<endl<<"------------------------------------------------------"<<endl;
    flag2 = randomInputGenerator(n);
    if(!flag2)
    {
        cout<<"Could not write into file.Error.";
        return 0;
    }
    bool flag = trie_1.load();
    cout<<endl<<"------------------------------------------------------"<<endl;
    if(flag)
    {
        cout<<endl<<"SUCCESSFULLY LOADED DICTIONARY INTO TRIE!!"<<endl;
    }
    else
    {
        cout<<endl<<"COULD NOT LOAD THE DICTIONARY INTO THE TRIE"<<endl;
        return 0;
    }
    do
    {
      cout<<endl<<"------------------------------------------------------"<<endl;
      cout<<endl<<"TRIE MENU"<<endl;
      cout<<endl<<"------------------------------------------------------"<<endl;
      cout<<endl<<"1. Search for a given word."<<endl;
      cout<<endl<<"2. Get the number of words in the dictionary. "<<endl;
      cout<<endl<<"3. Print trie nodes."<<endl;
      cout<<endl<<"4. Load dictionary."<<endl;
      cout<<endl<<"5. Insert a new word into the trie."<<endl;
      cout<<endl<<"6. Delete a word from the trie."<<endl;
      cout<<endl<<"0. EXIT"<<endl;
      cout<<endl<<"------------------------------------------------------"<<endl;
      cout<<endl<<"Enter your choice: ";
      cin>>choice;
      cout<<endl<<"------------------------------------------------------"<<endl;

      switch(choice)
      {
          case 1:
              cout<<endl<<"Enter the string you want to search for : ";
              cin>>tosearch;
              flag2 = trie_1.searchWord(tosearch);
              cout<<endl<<"------------------------------------------------------"<<endl;
              if(flag2)
              {
                cout<<endl<<"THE GIVEN WORD IS PRESENT IN THE DICTIONARY!!!";
              }
              else
              {
                cout<<endl<<"THE GIVEN WORD IS NOT IN THE DICTIONARY!!!";
              }
              break;

          case 2:
              cout<<endl<<"------------------------------------------------------"<<endl;
              cout<<endl<<"THE NUMBER OF WORDS IN THE DICTIONARY ARE: ";
              cout<<trie_1.size();
              break;

          case 3:
              flag2 = trie_1.printNodes();
              cout<<endl<<"------------------------------------------------------"<<endl;
              if(flag2)
              {
                  cout<<" SUCCESSFLLY PRINTED FROM THE TRIE!!";
              }
              else
              {
                  cout<<"UNLOADING UNSUCCESSFUL!!";
              }
              break;

          case 4:
              flag2 = trie_1.load();
              cout<<endl<<"------------------------------------------------------"<<endl;
              if(flag2)
              {
                  cout<<endl<<"SUCCESSFULLY LOADED DICTIONARY INTO TRIE!!!"<<endl;
              }
              else
              {
                  cout<<endl<<"COULD NOT LOAD DICTIONARY INTO TRIE!!!"<<endl;
              }
              break;

          case 5:
              cout<<endl<<"Enter the word to insert :  ";
              cin>>toinsert;
              flag = trie_1.insertNewWord(toinsert);
              cout<<endl<<"------------------------------------------------------"<<endl;
              if(flag)
              {
                  cout<<endl<<toinsert<<" IS SUCCESSFULLY INSERTED INTO THE TRIE.";
              }
              else
              {
                  cout<<endl<<toinsert<<" IS ALREADY IN THE TRIE.";
              }
              break;

          case 6:
              cout<<endl<<"Enter the word to delete : ";
              cin>>todelete;
              flag = trie_1.deleteWord(todelete);
              cout<<endl<<"------------------------------------------------------"<<endl;
              if(flag)
              {
                  cout<<endl<<todelete<<" IS SUCCESSFULLY DELETED FROM THE TRIE.";
              }
              else
              {
                  cout<<endl<<todelete<<" IS NOT PRESENT IN THE TRIE.";
              }
              break;

          case 0:
              cout<<"BYE!!!";
              cout<<endl<<"------------------------------------------------------"<<endl;
              break;

          default :
              cout<<endl<<"------------------------------------------------------"<<endl;
              cout<<"WRONG INPUT!!TYPE YOUR OPTION AGAIN!!";
              break;

      }
    }while (choice != 0);

    return 0;

}

bool Trie::searchWord(const char *word)
{
    node *temp = root;
    for (int i = 0, n = strlen(word); i < n; i++)
    {

        if (word[i] == '\'')
        {

            if (temp->children[0] == NULL)
            {
                return false;
                break;
            }
            else
            {
                temp = temp->children[0];
                if (i == n - 1 && temp->is_word == true)
                {
                    return true;
                }
                if (i == n - 1 && temp->is_word == false)
                {
                    return false;
                }
            }
            continue;
        }

        int x;
        int ch;
        ch = toupper(word[i]);
        x = ch - 64;
        if (temp->children[x] == NULL)
        {
            return false;
            break;
        }
        else
        {
            temp = temp->children[x];
            if (i == n - 1 && temp->is_word == true)
            {
                return true;
            }
            if (i == n - 1 && temp->is_word == false)
            {
                return false;
            }
        }

    }

    delete temp;
    return false;

}

bool Trie::load()
{
    char word[45 + 1];//Maximum size of a word is 45(FACT)
    ifstream fin;
    fin.open("input.txt");

    if (!fin)
    {
        cout<<"COULD NOT OPEN THE FILE";
        return false;
    }
    else
    {

        root = new node;
        for (int z=0;z<27;z++)
        {
            root->children[z]=NULL;
        }
        while (true)
        {
            fin>>word;
            if(fin.eof())
            {
                break;
            }
            cout<<word<<endl;
            j++;
            node *temp = root;
            for (int i = 0, n = strlen(word); i < n; i++)
            {

                if (word[i] == '\'')
                {
                    if (temp->children[0] == NULL)
                    {
                        temp->children[0] = new node;
                        for (int z=0;z<27;z++)
                        {
                             temp->children[0]->children[z]=NULL;
                        }
                        temp = temp->children[0];
                        if (i == n - 1)
                        {
                            temp->is_word = true;
                        }
                    }
                    else
                    {
                        temp = temp->children[0];
                        if (i == n - 1)
                        {
                            temp->is_word = true;
                        }
                    }
                    continue;
                }
                int x;
                int ch;
                ch = toupper(word[i]);
                x = ch - 64;
                if (temp->children[x] == NULL)
                {
                    temp->children[x] = new node;
                    for (int z=0;z<27;z++)
                    {
                         temp->children[x]->children[z]=NULL;
                     }
                    temp = temp->children[x];
                    if (i == n - 1)
                    {
                        temp->is_word = true;
                    }
                }
                else
                {
                    temp = temp->children[x];
                    if (i == n - 1)
                    {
                        temp->is_word = true;
                    }
                }

            }

            temp = NULL;
            delete temp;

        }
        fin.close();
        return true;
    }
}

unsigned int Trie::size()
{

    if (j > 1)
    {
        return j - 1;
    }
    return 0;
}


bool Trie::printNodes()
{


    for (int i = 0; i < 27; i++)
    {
        if (root->children[i] != NULL)
        {
	          cout<<(char)(i+64)<<" "<<endl;
            freeNode(root->children[i]);

        }
    }
    // delete root;
    // j=1;

    return true;
}

void Trie::freeNode(node *currentNode)
{

    for (int i = 0; i < 27; i++)
    {
        if (currentNode->children[i] != NULL)
        {
	    cout<<(char)(i+64)<<" "<<endl;
            freeNode(currentNode->children[i]);

        }
    }
    // currentNode = NULL;
    // delete currentNode;

}

bool Trie::insertNewWord(const char *word)
{
    if(!searchWord(word))
    {
        j++;
        node *temp = root;
        for (int i = 0, n = strlen(word); i < n; i++)
        {

            if (word[i] == '\'')
            {
                if (temp->children[0] == NULL)
                {
                    temp->children[0] = new node;
                    temp->children[0]->is_word = false;
                    for (int z=0;z<27;z++)
                    {
                         temp->children[0]->children[z]=NULL;
                    }
                    temp = temp->children[0];
                    if (i == n - 1)
                    {
                        temp->is_word = true;
                    }
                }
                else
                {
                    temp = temp->children[0];
                    if (i == n - 1)
                    {
                        temp->is_word = true;
                    }
                }
                continue;
            }
            int x;
            int ch;
            ch = toupper(word[i]);
            x = ch - 64;
            if (temp->children[x] == NULL)
            {
                temp->children[x] = new node;
                temp->children[x]->is_word = false;
                for (int z=0;z<27;z++)
                {
                     temp->children[x]->children[z]=NULL;
                 }
                temp = temp->children[x];
                if (i == n - 1)
                {
                    temp->is_word = true;
                }
            }
            else
            {
                temp = temp->children[x];
                if (i == n - 1)
                {
                    temp->is_word = true;
                }
            }

        }

        temp = NULL;
        delete temp;
        return true;
    }
    else
    {
        return false;
    }
}

bool Trie::deleteWord(const char *word)
{
    node *temp = root;
    for (int i = 0, n = strlen(word); i < n; i++)
    {

        if (word[i] == '\'')
        {

            if (temp->children[0] == NULL)
            {
                return false;
                break;
            }
            else
            {
                temp = temp->children[0];
                if (i == n - 1 && temp->is_word == true)
                {
                    temp->is_word = false;
                    --j;
                    return true;
                }
                if (i == n - 1 && temp->is_word == false)
                {
                    return false;
                }
            }
            continue;
        }

        int x;
        int ch;
        ch = toupper(word[i]);
        x = ch - 64;
        if (temp->children[x] == NULL)
        {
            return false;
            break;
        }
        else
        {
            temp = temp->children[x];
            if (i == n - 1 && temp->is_word == true)
            {
                temp->is_word = false;
                --j;
                return true;
            }
            if (i == n - 1 && temp->is_word == false)
            {
                return false;
            }
        }

    }

    delete temp;
    return false;

}

bool randomInputGenerator(int n)
{
    ofstream fout;
    fout.open("input.txt");
    if(!fout.is_open())
    {
        cout<<"Could not open the file";
        return false;
    }
    int lf,i,j;
    srand(time(0));
    string word;
    for(int i=0;i<n;i++)
    {
        lf=1+rand()%45;
        word="";
        for(int j=0;j<lf;j++)
            word.push_back(char(97+rand()%26));
        fout<<word<<endl;
    }
    fout.close();
    return true;
}
