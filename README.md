# ToMNet 2.0 Project

## Overview
*By Jessica Le, 16 July 2023*

Advanced AI chatbots are becoming widely used across many different platforms to provide innovative user interfaces. Industries, such as marketing and ecommerce, have integrated these chatbots into websites and applications to create personalized AI experiences to help answer queries. Currently, these interfaces occur solely between the chatbox and the user in an artificial one on one conversation. While some chat boxes have become more and more human-like, AI lacks emotional intelligence and understanding of social contexts. However, what if chat boxes were able to process human social preferences so that they would be able to understand the dynamic between multiple people in a social setting. Such social machines would have greater potential to create more naturalistic human-machine interactions. 

For example, say a user would like to use a chat box to express deeper feelings beyond shopping queries or homework help. In the simple case below, the user expresses their mental health situation and asks the chat box to speak to a friend. 

ToMnet 2.0 is a proof of concept project that aims to use machine Theory of Mind for processing complex social networks. This artificial neural network is an adaptation of  ToMnet+ (published in 2020 by Yun-Shuin et al.), which uses machine theory of mind to predict social preferences based on implicit information from the way agents and social targets interact behaviorally. However, ToMnet+ is one dimensional such that it is limited to only considering one agent’s preference towards other targets at a time. Real life interactions are almost never one sided and can be very complex between groups of people. 

Using ToMnet+’s inferences of hidden information structures from a third person observation of behavior, ToMnet 2.0 interprets five agent’s social preferences simultaneously. This model is trained by a set of five body social problem simulation and reconstructs the embedded social preferences. The goal is for ToMnet 2.0 to be able to predict and distinguish different sets of social preferences, as well as be able to predict very similar social behaviors provided by simulation data. 

Below is a diagram representation of the character and prediction network used in ToMnet 2.0. The character network extracts an abstract representation of the agent’s (ai) preference for other agents (Ji) and outputs a character embedding called echar, j. The prediction network takes in  echar, j and qk (a query state indicating direction of trajectory) and predicts the target that the agent is most likely to have a preference, yielding gk. 

Social preferences are difficult to read, as there is often a disconnection between people’s intentions, actions, and genuine feelings. ToMnet 2.0 can be applied in many different contexts such as [TO DO: provide some example applications: mental health chat boxes, empathetic robots etc] If you use this repository, please cite [1].

## Key directories in this repo
- **data**: simulation maze data for ToMNet 2.0
- **model**: ToMNet 2.0 model.
- **reports**: Slides, documents, progress updates
- **scripts**: Codes for maze data generation, ToMNet 2.0 output data analysis, plotting.

## Related Reports
- Yen-Ling Lai's [Master's thesis](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/blob/master/reports/thesis)
- [Proposal slides](https://docs.google.com/presentation/d/1aBJ_AeC3MMow27sem7PYY1u2AObtxEcQtJsQubjBxG0/edit)
- Talk by Josh @ Taiwan Chinese Psychology Society Meeting 2022 [[pptx]](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/blob/master/report/ToMNet_Taiwan_Chinese_Psychology_Meeting.pptx)[[resources]](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/tree/master/report/%E5%BF%83%E7%90%86%E7%B5%84%E6%9C%83)
- Prof. Li-Chen Fu 2023 Apr 6 progress report draft to NSTC [[pdf]](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/blob/master/report/CM03_%E6%9C%80%E6%9C%80%E7%B5%82%E7%89%88v3.pdf)
    - Josh sub-section [[docx]](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/blob/master/report/111%E5%B9%B4%E5%BA%A6%E5%B7%A5%E7%A8%8B%E7%A7%91%E6%8A%80%E4%B8%AD%E5%A0%85%E8%BA%8D%E5%8D%87%E7%A0%94%E7%A9%B6%E8%A8%88%E7%95%AB-JG.docx)[[pptx]](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/blob/master/report/111%E5%B9%B4%E5%BA%A6%E5%B7%A5%E7%A8%8B%E7%A7%91%E6%8A%80%E4%B8%AD%E5%A0%85%E8%BA%8D%E5%8D%87%E7%A0%94%E7%A9%B6%E8%A8%88%E7%95%AB-JG.pptx)

## Discord
https://discord.com/channels/1070259860026957915/1070387486536253490

## Usage tutorial
- See [tomnet2_jl](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2_jl), master branch. Note: This project repo was copied by JL based on a previous state of tomnet2 repo. There are possible unmerged content changes.
- See [TUTORIAL.md](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/tomnet2/-/blob/master/TUTORIAL.md)

## Application to human data (AVALON RPG)
See [TOMAV](https://gitlab.com/brain-and-mind-lab/research-projects/tomnet/TOMAV)

## Bibliography
[1] Chuang, Y.S., Hung, H.Y., Gamborino E., Goh, O.S., Huang, T.R., Chang, Y.L., Yeh, S.L., Fu,L.C. (2020) Using Machine Theory of Mind to Learn Agent Social Network Structures from Observed Interactive Behaviors with Targets. IEEE, Robot and Human Interactive Communication [url](https://ieeexplore.ieee.org/abstract/document/9223453)<br>
[2] ToMNet-plus Github repository [url](https://github.com/NTUBMLab/tomnet-plus)
