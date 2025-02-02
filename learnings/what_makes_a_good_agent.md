# What makes a good Agent.

### Role Playing

Tell the agent how they should behave. For example:

W/o role playing: Give me an analysis of the TESLA stock

Wit role playing: You are an finantial analystics from Deloitte. Give me an analysis of the TESLA stock

### Focus

It's better when an agent is focused in a single task instead of doing too many things. For example:

W/o focus: if the goal is to right a blog post. Create one single agent to research, write and edit the blog post

Wit role playing: if the goal is to right a blog post. Create one agent to research, one to write and one to edit.

### Tools

Agent using better tooling makes sure they will produce better results. Using one of a few tools per agent is also recommended to keep focus of the agent.

### Colaboration

Since it's recommended to have focused agent, for complex tasks, collaboration among agent is a must.

### Guardrails

Setting guardrails will prevent the models from operate in an undisered way. For instance, Crew AI has added a few guardrails to prevent smaller models to get stuck on a step that prevents the agent from completing a task.

### Memory

The ability that your agent has to remember what they did in the past and learn from them.

#### Short Term Memory

Lives only during crew execution and will be shared accross multiple agents. That's super important to share context towards a goal.

#### Long Term Memory

Lives in a separate database and it can shared accross different crew executions. Useful to store memory for future crew runs.

#### Entity Memory

Very similar to short term memory, but it's related to the subjects of a crew execution
